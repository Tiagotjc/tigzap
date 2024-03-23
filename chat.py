import flet 

def main(pagina):
    texto=flet.Text("Tigzap")




    chat = flet.Column()

    def enviar_mensagem_tunel (mensagem):
        print("enviou mensagem no tunel")

        texto_mensagem = flet.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        print("Enviar mensagem")
        pagina.pubsub.send_all(f"{nome_usuario.value}:{campo_mensagem.value}")
        #add mensagem
        
        #limpe campo
        campo_mensagem.value = ""


        pagina.update()

    

    campo_mensagem = flet.TextField(label="Digite dua mensagem:", on_submit= enviar_mensagem)
    botao_enviar= flet.ElevatedButton("Enviar",on_click=enviar_mensagem)
    linha_enviar = flet.Row([campo_mensagem,botao_enviar])
    def entrar_chat(evento):
        print("Entrar no chat")
        popup.open = False
        pagina.remove(texto)
        pagina.remove(botao_iniciar)
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
       
        
        pagina.add(linha_enviar)

        pagina.update()


    titulo_popup = flet.Text("Seja bem vindo ao Tigzap")
    nome_usuario = flet.TextField(label="Digite seu nome ao chat:")
    botao_entrar= flet.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    popup = flet.AlertDialog(
        open=False,
        modal=True,
        title= titulo_popup,
        content= nome_usuario,
        actions= [botao_entrar] 
    )
     
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()


    botao_iniciar = flet.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    
    
    
    
    pagina.add(texto)
    pagina.add(botao_iniciar)




flet.app(target=main, view=flet.WEB_BROWSER)
