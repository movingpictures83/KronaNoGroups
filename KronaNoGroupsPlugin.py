class KronaNoGroupsPlugin:
    def input(self, filename):
       self.infile = open(filename, 'r')

    def run(self):
       self.lines = []
       for line in self.infile:
           contents = line.strip().split('\t')
           newcontents = []
           for i in range(0, len(contents)):
               if ("group" not in contents[i]):
                   newcontents.append(contents[i])
           newline = ""
           for i in range(0, len(newcontents)):
               newline += newcontents[i]
               if (i == len(newcontents)-1):
                   newline += "\n"
               else:
                   newline += "\t"
           self.lines.append(newline)

    def output(self, filename):
        self.outfile = open(filename, 'w')
        for line in self.lines:
            self.outfile.write(line)

