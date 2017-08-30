from django.core.management.base import BaseCommand
from lxml.html import parse
from datetime import datetime
from agenda.models import Evento, Local
from politicos.models import Politico, Partido



class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'
    
    def _scrape(self):
        url = "http://www.camara.sp.gov.br/atividade-legislativa/agenda-da-camara/"

        soup = parse(url)
        soup = soup.getroot()

        lista_dias = soup.cssselect(".agenda-events-list article h2")
        agenda = []
        for d in lista_dias:
            dia = d.text.strip()
            lista_eventos = d.getnext().cssselect(".agenda-event")
            for e in lista_eventos:
                evento = {}
                evento['data'] = dia
                evento['descricao'] = e.cssselect("td.event")[0].text_content().strip()
                evento['autor'] = e.cssselect("td.vereador")[0].text_content().strip()
                evento['partido'] = None;
                if e.cssselect("td.party img"):
                    evento['partido'] = e.cssselect("td.party img")[0].get('title')
                evento['local'] = e.cssselect("td.location a")[0].text_content().strip()
                agenda.append(evento)
        return agenda

    def _create_events(self, agenda):
        for item in agenda:
            local, created = Local.objects.update_or_create(nome = item['local'])
            local.save()
            
            if item['partido']:
                partido, created = Partido.objects.update_or_create(sigla = item['partido'])
                partido.save()
            else:
                partido = None
            
            politico, created = Politico.objects.update_or_create(nome = item['autor'], partido=partido)
            politico.save()
            
            data = datetime.strptime(item['data'], '%d/%m/%Y')
            evento = Evento(vereador=politico, local=local, descricao=item['descricao'], data=data)
            evento.save()
    
    def handle(self, *args, **options):
        agenda = self._scrape()
        self._create_events(agenda)