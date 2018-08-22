
def read_speaker_file(path):
    f = open(path, "r")
    lines = f.readlines()
    #speak_dict 
    speak_sched = []
    for line in lines:
        script = dict()
        contents = line.split(',')
        script['id']= contents[0]
        script['group_nickname'] = contents[1]
        script['time'] = contents[2]
        script['msg'] = contents[3]
        speak_sched.append(script)
    return speak_sched
    
        
        

