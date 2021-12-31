# import re

# important_lines = []

# with open('log\COM12_21-347-22-51_output.log', 'r') as f:
#     for line in f:
#         if "INFO" in line:
#             if "devkey_handle" in line:
#                 print(line)
#                 index = line.index("devkey_handle")
#            #     print (index)
#                 buffer = line[index + 16:]
#                 out = buffer.split("}")[0]
#                 print(out)
                
      #      print (line)


class Logdocument:
    def __init__(self):
        index = 0
        buffer = ""

    def get_info_lines(self, log_file: str) -> list[str]: #list = return type
        INFO_LINES=[]
        with open(log_file, 'r') as f:
            for line in f:
                if 'INFO' in line:
                    INFO_LINES.append(line)
        return INFO_LINES

    def parse_devkey(self, line: str) -> int: #int = return type
        index = line.index("devkey_handle")
        buffer = line[index + 16:]
        return int(buffer.split("}")[0])

    def parse_addrehandle(self, line: str) -> int: #int = return type
        index = line.index("address_handle")
        buffer = line[index + 16:] 
        return int(buffer.split("}")[0])

    def main(self):
        lines = get_info_lines('log\COM12_21-347-22-51_output.log')
        for line in lines:
            if 'devkey_handle' in line: #zit devkey_handle in die line
                print(f'Devkey: {parse_devkey(line)}') #print de nummer van devkey
            elif 'address_handle' in line:
                print(f'address_handle: {parse_addrehandle(line)}')

#if __name__ == '__main__':
 #  Logdocument()
  #  main()
            
