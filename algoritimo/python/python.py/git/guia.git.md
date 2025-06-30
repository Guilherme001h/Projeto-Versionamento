# Comando "git"

## O comando git é usado para controlar versões de arquivos em projetos, principalmente em programação. Ele permite que você registre todas as mudanças feitas no código ao longo do tempo, colabore com outras pessoas e mantenha o histórico completo do que foi feito. Quando você usa o Git, todo o repositório (ou seja, todos os arquivos e o histórico de versões) fica armazenado localmente no seu computador, e você pode sincronizá-lo com servidores online como o GitHub.

## Você começa um repositório com o comando git init, que cria a pasta oculta .git e começa a rastrear alterações. Se você já tem um projeto online, como no GitHub, pode usar git clone seguido do link do repositório para copiá-lo para o seu computador.

## Quando você modifica arquivos, o Git não salva automaticamente essas mudanças. Primeiro você precisa preparar os arquivos para o commit com git add. Isso coloca os arquivos na “área de staging”. Depois, você executa git commit -m "mensagem" para salvar as alterações com uma descrição. Isso cria um ponto no histórico do projeto ao qual você pode voltar depois se precisar.

## Se você estiver colaborando com outras pessoas ou quer manter um backup online, usa git push para enviar suas mudanças para um servidor remoto como o GitHub. E quando alguém muda algo no repositório remoto, você usa git pull para trazer essas mudanças para o seu repositório local.

## Para ver o que está acontecendo, você pode usar git status, que mostra quais arquivos foram modificados, adicionados ou estão prontos para commit. Se quiser ver o histórico de alterações feitas no projeto, git log mostra uma lista de commits com autor, data e mensagem.

## Com o Git, você também pode criar ramificações chamadas branches com git branch. Isso permite trabalhar em funcionalidades diferentes sem afetar o código principal. Para mudar de uma branch para outra, você usa git checkout, e quando quiser juntar o que fez em uma branch com outra, usa git merge.

## O Git é muito poderoso e evita perder trabalhos, facilita voltar a versões anteriores e ajuda bastante no trabalho em equipe. Tudo que você faz com git acontece com segurança no seu computador primeiro, e só vai para a nuvem quando você quiser.
