from mycroft import MycroftSkill, intent_file_handler


class CpuPerc(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('perc.cpu.intent')
    def handle_perc_cpu(self, message):
        self.speak_dialog('perc.cpu')


def create_skill():
    return CpuPerc()

