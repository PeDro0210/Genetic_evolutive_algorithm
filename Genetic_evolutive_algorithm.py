from pydub import AudioSegment
from pydub.playback import play
import random as rd
import os 

direcotory = 'music'
songs = []
durations = []
#it has to be on mp3 format
for i in os.listdir(direcotory):
    song = AudioSegment.from_file(f"music\\{i}", format="mp3")
    songs.append(song)


for i in songs:
    durations.append(len(i))


all_audios=[]


def separating_segmentes(audio_file, duration):
    segmentes = []
    segment_duration=50000
    
    number_of_segments = duration//segment_duration
    
    for i in range(number_of_segments):
        start= i*segment_duration
        end = start+segment_duration
        segment=audio_file[start:end]
        segmentes.append(segment)
    return segmentes    




def concatenating_segments(fitness, song_name):
    concatenated_audio = AudioSegment.empty()
    for segment in fitness:
        concatenated_audio=concatenated_audio + segment
        
    concatenated_audio.export(f"Created_music\\{song_name}.mp3", format="mp3")
    return concatenated_audio


def concatenating_segments_checker(fitness):
    concatenated_audio = AudioSegment.empty()
    for segment in fitness:
        concatenated_audio=concatenated_audio + segment
        
    return concatenated_audio




for i in range(len(songs)):
    song = songs[i]
    duration = durations[i]
    Usable_song = separating_segmentes(song, duration)
    all_audios.append(Usable_song)




def fitness_dbs(all_audios):
    fitness = []
    
    
    base_segment = all_audios[rd.randint(0,len(all_audios))-1][rd.randint(0,len(all_audios[0]))-1]
    
    fitness.append(base_segment)


        
    for i in range(len(all_audios)):
        
        
        song = all_audios[rd.randint(0,len(all_audios)-1)]
        song2 = all_audios[rd.randint(0,len(all_audios)-2)]
        
        for j in range(len(song)//2):
            segment = song[rd.randint(0,len(song)-1)]
            segment2 = song2[rd.randint(0,len(song2)-1)]
        
            if segment not in fitness or segment2 not in fitness:
                if segment!=segment2:         
                    if segment.frame_rate>segment2.frame_rate:
                        
                        fitness.append(segment)
                        fitness.append(segment2)
                        
                        if segment.dBFS > segment2.dBFS:
                            fitness.append(segment)
                            fitness.append(segment2)
                        else:
                            fitness.append(segment2)
                            fitness.append(segment)
                    else:
                        
                        fitness.append(segment2)
                        fitness.append(segment)
                        
                        if segment.dBFS > segment2.dBFS:
                            fitness.append(segment)
                            fitness.append(segment2)
                        else:
                            fitness.append(segment2)
                            fitness.append(segment)
                else:
                    pass     
            else:
                pass     
            
    return fitness
    
    




for i in range(10):
    o=True
    while o:
        
        if  len(concatenating_segments_checker(fitness_dbs(all_audios)))<len(concatenating_segments_checker(fitness_dbs(all_audios)))*0.5 :
            print(f"not done {len(concatenating_segments_checker(fitness_dbs(all_audios)))}")
            separating_segmentes(concatenating_segments_checker(fitness_dbs(all_audios)), len(concatenating_segments_checker(fitness_dbs(all_audios))))
            
        else:
            #aqui ya crea la cancion y listo
            print(f"done {len(concatenating_segments_checker(fitness_dbs(all_audios)))}")
            concatenating_segments(fitness_dbs(all_audios), f"song{i}")
            o=False

