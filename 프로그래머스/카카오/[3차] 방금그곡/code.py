from datetime import datetime
def solution(m, musicinfos):
    m = change(m)
    result = []
    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(',')
        title = musicinfo[2]
        start_time = datetime.strptime(musicinfo[0], "%H:%M")
        end_time = datetime.strptime(musicinfo[1], "%H:%M")
        play_time= int((end_time - start_time).total_seconds() // 60)
        sounds = total_sound(play_time, musicinfo[3])
        
        if m in sounds:
            result.append([title, play_time])
            
    if len(result) == 0:
        return "(None)"
    else:
        result.sort(key=lambda x : x[1], reverse=True)
        result=[title for title, _ in result]
        return result[0]
    

    
def total_sound(play_time,sounds):
    sounds = change(sounds)
    q,r = divmod(play_time, len(sounds))
    sounds = (sounds * q) + sounds[:r]
    return sounds


def change(m):
    changes= {'A#':'a', 'C#':'c', 'D#':'d', 'F#':'f', 'G#':'g'}
    for sound in changes:
        m = m.replace(sound, changes[sound])

    return m