from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        #Open Discord app to send a message to a friend.
        self.execute(r'C:\Users\thiag\OneDrive\Área de Trabalho\Discord.lnk')
        if not self.find( "Search", matching=0.97, waiting_time=20000):
            self.not_found("Search")
        self.click()
        self.paste("alucadiel")
        if not self.find( "alucadielbot", matching=0.97, waiting_time=20000):
            self.not_found("alucadielbot")

        self.click()
        #send a youtube link video to this friend
        self.paste("https://www.youtube.com/watch?v=pEtFm4OWo5g")
        self.enter()
        #paste a message which contains :  see you later,  Thiago Galhardo video sent by a bot via python
        self.paste("vídeo do até logo, thiago galhardo enviado por um bot via python")
        self.enter()
    # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
