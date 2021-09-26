from driver import Driver
from pprint import pprint as pp
from pdb import set_trace as trace

class Workshop(Driver):
    def process_file(self, p):
        super().process_file(p)

    # def run(self):
    #     super().run()
        # print('Hello world')
        # self.cmdloop()

    def do_new(self, args):
        print("Creating a new project...")
