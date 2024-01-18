from plyer import notification
from datetime import datetime

def Alerta(nivel, base, etapa):
    titulo = 0
    data = datetime.now()
   
    if nivel == 1:
        titulo = 'Alerta Baixo'
    elif nivel == 2:
        titulo = 'Alerta Médio'
    elif nivel == 3:
        titulo = 'Alerta Alto'



    notification.notify(
    title = titulo,
    message = f'Falha no carregamento da base {base} na etapa {etapa}\
          {data}',
    app_name = '',
    timeout = 5)

Alerta(1,'Produtos','Cadastro')