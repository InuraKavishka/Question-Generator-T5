# pip install -U textblob
# pip install flashtext
# get_ipython().system('pip install -U pywsd')
# pip install -U wn==0.0.22

import nltk
nltk.download('brown')
nltk.download('punkt')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('brown')
import nltk
nltk.download('wordnet')


summarized_text = 'The Nile River fed Egyptian civilization for hundreds of years. It begins near the equator in Africa and flows north to the Mediterranean Sea. This soil was fertile, which means it was good for growing crops. The red land was the barren desert beyond the fertile region. When the birds arrived, the annual flood waters would soon follow. Then they used a tool called a shaduf to spread the water across the fields. They were the first to grind wheat into flour and to mix the flour with yeast and water to make dough rise into bread. Egyptians often painted walls white to reflect the blazing heat. Poorer Egyptians simply went to the roof to cool off after sunset. Nubia was the Egyptian name for the area of the upper Nile that had the richest gold mines in Africa. Even during the cool season, chipping minerals out of the rock was miserable work. One ancient painting even shows a man ready to hit a catfish with a wooden hammer. A boomerang is a curved stick that returns to the person who threw it.) Eventually, Egyptians equipped their reed boats with sails and oars. Going south, they raised a sail and let the winds that blew in that direction push them. The Nile provided so well for Egyptians that sometimes they had surpluses, or more goods than they needed. Ancient Egypt had no money, so people exchanged goods that they grew or made. This prosperity made life easier and provided greater opportunities for many Egyptians. For example, some ancient Egyptians learned to be scribes, people whose job was to write and keep records. Some skilled artisans erected stone or brick houses and temples. These traders took Egyptian products such as scrolls, linen, gold, and jewelry. Egyptians created a government that divided the empire into 42 provinces. Before entering a temple, a priest bathed and put on special linen garments and white sandals. So the ruler and the priests tried hard to keep the gods happy. By doing so, they hoped to maintain the social and political order. In Egypt, people became slaves if they owed a debt, committed a crime, or were captured in war. Unlike other ancient African cultures, in Egyptian society men and women had fairly equal rights. For example, they could both own and manage their own property. Children in Egypt played with toys such as dolls, animal figures, board games, and marbles. Almost all Egyptians married when they were in their early teens. Doctors believed that the heart controlled thought and the brain circulated blood, which is the opposite of what is known now. Early Egyptians created a hieroglyphic system with about 700 characters. Egyptians cut the stems into strips, pressed them, and dried them into sheets that could be rolled into scrolls. Legend says a king named Narmer united Upper and Lower Egypt. Some historians think Narmer actually represents several kings who gradually joined the two lands. It combined the red Crown of Lower Egypt with the white Crown of Upper Egypt. When a king died, one of his children usually took his place as ruler. The order in which members of a royal family inherit a throne is called the succession. Historians divide ancient Egyptian dynasties into the Old Kingdom, the Middle Kingdom, and the New Kingdom. Because the pharaoh was thought to be a god, government and religion were not separate in ancient Egypt. The first rulers of Egypt were often buried in an underground tomb topped by mud brick. They replaced the mud brick with a small pyramid of brick or stone. It is called a step pyramid because its sides rise in a series of giant steps. He ordered the construction of the largest pyramid ever built. Miners cut the huge blocks of stone using copper saws and chisels. One reason is that the pyramids drew attention to the tombs inside them. Grave robbers broke into the tombs to steal the treasure buried with the pharaohs. Egyptians believed that if a tomb was robbed, the person buried there could not have a happy afterlife. During the New Kingdom, pharaohs began building more secret tombs in an area called the Valley of the Kings. This was to confuse grave robbers about which passage to take. Sometimes relatives, such as the queen, were buried in the extra rooms. Tombs were supposed to be the palaces of pharaohs in the afterlife. Mourners filled the tomb with objects ranging from food to furniture that the mummified pharaoh would need. A sculpture of a dead pharaoh had “perfect” features, no matter how he really looked. Artists also followed strict rules about how to portray humans. Such activities included growing and preparing food, caring for animals, and building boats. Only a secret tomb built for a New Kingdom pharaoh was ever found with much of its treasure untouched. The dazzling riches found in this tomb show how much wealth the pharaohs spent preparing for the afterlife. By about 2130 B.C., Egyptian kings began to lose their power to local rulers of the provinces.'

summarized_text = 'Bob greene: president obama gave a speech to the 19th national boy scout jamboree. he says he went predictably off-script to talk about some favourite topics. greene: scouts believe in putting america first; vp was a scout and it meant so much to him. he says if he gets the votes to kill obamacare, hell be a big help to scout'

# f = open("egypt.txt","r")
# full_text = f.read()

full_text = 'Hotels in Mumbai and other Indian cities are to train their staff to spot signs of sex trafficking such as frequent requests for bed linen changes or a "Do not disturb" sign left on the door for days on end. The group behind the initiative is also developing a mobile phone app - Rescue Me - which hotel staff can use to alert local police and senior anti-trafficking officers if they see suspicious behavior. "Hotels are breeding grounds for human trade," said Sanee Awsarmmel, chairman of the alumni group of Maharashtra State Institute of Hotel Management and Catering Technology. "(We) have hospitality professionals working in hotels across the country. We are committed to this cause."The initiative, spearheaded by the alumni group and backed by the Maharashtra state government, comes amid growing international recognition that hotels have a key role to play in fighting modern day slavery. MAHARASHTRA MAJOR DESTINATION FOR TRAFFICKED GIRLS Maharashtra, of which Mumbai is the capital, is a major destination for trafficked girls who are lured from poor states and nearby countries on the promise of jobs, but then sold into the sex trade or domestic servitude. With rising property prices, some traditional red light districts like those in Mumbai have started to disappear pushing the sex trade underground into private lodges and hotels, which makes it hard for police to monitor.Awsarmmel said hotels would be told about 50 signs that staff needed to watch out for.These include requests for rooms with a view of the car park which are favored by traffickers as they allow them to vet clients for signs of trouble and check out their cars to gauge how much to charge.Awsarmmel said hotel staff often noticed strange behavior such as a girls reticence during the check-in process or her dependence on the person accompanying her to answer questions and provide her proof of identity.But in most cases, staff ignore these signs or have no idea what to do, he told the Thomson Reuters Foundation.RESCUE ME APP The Rescue Me app - to be launched in a couple of months - will have a text feature where hotel staff can fill in details including room numbers to send an alert to police.Human trafficking is the worlds fastest growing criminal enterprise worth an estimated $150 billion a year, according to the International Labor Organization, which says nearly 21 million people globally are victims of forced labor and trafficking.Last year, major hotel groups, including the Hilton and Shiva Hotels, pledged to examine their supply chains for forced labor, and train staff how to spot and report signs of trafficking.Earlier this year, Mexico City also launched an initiative to train hotel staff about trafficking.Vijaya Rahatkar, chairwoman of the Maharashtra State Womens Commission, said the initiative would have an impact beyond the state as the alumni group had contact with about a million small hotels across India.The group is also developing a training module on trafficking for hotel staff and hospitality students which could be used across the country.ALSO READFYI | Legal revenge: Child sex trafficking survivors get School of Justice to fight their own battlesMumbai: Woman DJ arrested in high-profile sex racket case'

full_text = 'On Monday evening, Donald Trump gave a speech to the 19th National Boy Scout Jamboree in West Virginia. Although he came armed with a prepared speech about the merits of scouting ? each US president serves as the group?s honorary president ? and declared at the start that he would not talk about politics, Trump went predictably off-script to talk about some favourite topics. And politics.Boy, you have a lot of people. The press will say it?s about 200 people. It looks like about 45,000 people.Tonight we put aside all of the policy fights in Washington DC that you have been hearing about with the fake news and all of that ? Who the hell wants to talk about politics when I?m in front of the Boy Scouts?Today I said we oughta change it from the word swamp to the word cesspool or perhaps to the word sewer, but it?s not good.The scouts believe in putting America first.The vice-president of the United States, Mike Pence ? good guy ? was a scout and it meant so much to him. Some of you here tonight might even have camped out in this yard when Mike was the governor of Indiana, but the scouting was very, very important. And by the way, where are our Indiana scouts tonight? I wonder if the television cameras will follow you; they don?t like doing that when they see these massive crowds. They don?t like doing that. Hi folks. A lot of love in this big, beautiful place. A lot of love and a lot of love for our country. There?s a lot of love for our country.By the way, what do you think the chances are that this incredible, massive crowd, record-setting, is going to be shown on television tonight? One per cent or zero? The fake media will say: President Trump ? and you know what this is ? President Trump spoke before a small crowd of Boy Scouts today. That?s some ? that is some crowd. Fake media. Fake news. Thank you.Secretary Tom Price is also here ? And hopefully he?s going to get the votes tomorrow to start our path toward killing this thing known as Obamacare that?s really hurting us, folks.By the way, are you going to get the votes? He better get them. He better get them. Oh, he better ? otherwise I?ll say, Tom, you?re fired. I?ll get somebody. He better get Senator Capito [Republican West Virginia senator Shelley Moore Capito] to vote for it. You got to get the other senators to vote for it. It?s time. After seven years of saying repeal and replace Obamacare, we have a chance to now do it. They better do it.By the way, just a question, did President Obama ever come to a jamboree? And we?ll be back. We?ll be back. The answer is no, but we?ll be back.I have to tell you our economy is doing great. Our stock market has picked up since the election November 8. Do we remember that date? Was that a beautiful date? What a date. Do you remember that famous night on television, November 8, where they said ? these dishonest people ? where they said there is no path to victory for Donald Trump? ? But do you remember that incredible night with the maps and the Republicans are red and the Democrats are blue, and that map was so red, it was unbelievable and they didn?t know what to say? And you know we have a tremendous disadvantage in the electoral college ? popular vote is much easier.So I have to tell you, what we did, in all fairness, is an unbelievable tribute to you and all of the other millions and millions of people that came out and voted for Make America Great Again.And by the way, under the Trump administration, you?ll be saying Merry Christmas again when you go shopping. Believe me. Merry Christmas. They?ve been downplaying that little beautiful phrase. You?re going to be saying Merry Christmas again, folks.I?ll tell you a story that?s very interesting for me when I was young. There was a man named William Levitt, Levitttowns, you have some here, you have some in different states ? And he was a very successful man. He was a homebuilder, became an unbelievable success, and got more and more successful ?And he sold his company for a tremendous amount of money. At the time especially, this was a long time ago, sold his company for a tremendous amount of money. And he went out and bought a big yacht and he had a very interesting life. I won?t go any more than that because you?re Boy Scouts, I?m not going to tell you what he did ? should I tell you? Should I tell you? Oh, you?re Boy Scouts, but you know life, you know life. So, look at you, who would think this is the Boy Scouts, right?So he had a very interesting life, and the company that bought his company was a big conglomerate. And they didn?t know anything about building homes, and they didn?t know anything about picking up the nails and the sawdust and selling it, and the scraps of wood ? So they called William Levitt up and they said, would you like to buy back your company and he said yes, I would. He so badly wanted it, he got bored with this life of yachts and sailing and all of the things he did in the south of France and other places ? But what happened is he bought back his company and he bought back a lot of empty land ? and in the end he failed and he failed badly. Lost all of his money. He went personally bankrupt, and he was now much older.And I saw him at a cocktail party and it was very sad. Because the hottest people in New York were at this party. It was the party of Steve Ross. Steve Ross, he was one of the great people. He came up and discovered ? really founded ? Time Warner, and he was a great guy. He had a lot of successful people at the party. And I was doing well]'

#summarized_text = 'Hotels in Maharashtra will train their staff to spot signs of sex trafficking, including frequent requests for bed linen changes and Do not disturb signs left on room doors for days. A mobile phone app called Rescue Me, which will allow staff to alert police of suspicious behaviour, will be developed. The initiative has been backed by the Maharashtra government'


# In[4]:


from textblob import TextBlob

blob_sum = TextBlob(summarized_text)
filtered_keys = blob_sum.noun_phrases

blob_full = TextBlob(full_text)
keywords = blob_full.noun_phrases

print(keywords)
print(filtered_keys)
print('----------')
print(len(keywords))
print(len(filtered_keys))

keywords = set(keywords)
keywords = list(keywords)

filtered_keys = set(filtered_keys)
filtered_keys = list(filtered_keys)
print(len(keywords))
print(len(filtered_keys))


# In[5]:


from nltk.tokenize import sent_tokenize
from flashtext import KeywordProcessor

def tokenize_sentences(text):
    sentences = [sent_tokenize(text)]
    sentences = [y for x in sentences for y in x]
    # Remove any short sentences less than 20 letters.
    sentences = [sentence.strip() for sentence in sentences if len(sentence) > 20]
    return sentences

def get_sentences_for_keyword(keywords, sentences):
    keyword_processor = KeywordProcessor()
    keyword_sentences = {}
    for word in keywords:
        keyword_sentences[word] = []
        keyword_processor.add_keyword(word)
    for sentence in sentences:
        keywords_found = keyword_processor.extract_keywords(sentence)
        for key in keywords_found:
            keyword_sentences[key].append(sentence)

    for key in keyword_sentences.keys():
        values = keyword_sentences[key]
        values = sorted(values, key=len, reverse=True)
        keyword_sentences[key] = values
    return keyword_sentences

sentences = tokenize_sentences(summarized_text)
print(sentences)
print(len(sentences))
for sentence in sentences:
    print(sentence)
    print('---')
keyword_sentence_mapping = get_sentences_for_keyword(filtered_keys, sentences)
        
#print (keyword_sentence_mapping)
for x in keyword_sentence_mapping:
    print(x)
    print('---**---')


# In[6]:


class QAdata:##object type
  def __init__(self, question, answer1, answer2, answer3, answer4, correctanswer):
    self.question = question
    self.answer1 = answer1
    self.answer2 = answer2
    self.answer3 = answer3
    self.answer4 = answer4
    self.correctanswer = correctanswer

class Answer:##object type
  def __init__(self, answer, status):
    self.answer = answer
    self.status = status


# In[25]:


from collections import OrderedDict
def sense2vec_get_words(word,s2v):
    output = []
    word = word.lower()
    word = word.replace(" ", "_")

    sense = s2v.get_best_sense(word)
    most_similar = s2v.most_similar(sense, n=20)

    # print ("most_similar ",most_similar)

    for each_word in most_similar:
        append_word = each_word[0].split("|")[0].replace("_", " ").lower()
        if append_word.lower() != word:
            output.append(append_word.title())

    out = list(OrderedDict.fromkeys(output))
    return out


# In[32]:


import requests
import json
import re
import random
from pywsd.similarity import max_similarity
from pywsd.lesk import adapted_lesk
from pywsd.lesk import simple_lesk
from pywsd.lesk import cosine_lesk
from nltk.corpus import wordnet as wn

# Distractors from Wordnet
def get_distractors_wordnet(syn,word):
    distractors=[]
    word= word.lower()
    orig_word = word
    if len(word.split())>0:
        word = word.replace(" ","_")
    hypernym = syn.hypernyms()
    if len(hypernym) == 0: 
        return distractors
    for item in hypernym[0].hyponyms():
        name = item.lemmas()[0].name()
        #print ("name ",name, " word",orig_word)
        if name == orig_word:
            continue
        name = name.replace("_"," ")
        name = " ".join(w.capitalize() for w in name.split())
        if name is not None and name not in distractors:
            distractors.append(name)
    return distractors

def get_wordsense(sent,word):
    print(sent)
    print(word)
    word= word.lower()
    
    if len(word.split())>0:
        word = word.replace(" ","_")
    
    synsets = wn.synsets(word,'n')
    
    if synsets:
        wup = max_similarity(sent, word, 'wup', pos='n')
        adapted_lesk_output =  adapted_lesk(sent, word, pos='n')
        lowest_index = min (synsets.index(wup),synsets.index(adapted_lesk_output))
        return synsets[lowest_index]
    else:
        return None

# Distractors from http://conceptnet.io/
def get_distractors_conceptnet(word):
    print(word)
    word = word.lower()
    original_word= word
    if (len(word.split())>0):
        word = word.replace(" ","_")
    distractor_list = [] 
    url = "http://api.conceptnet.io/query?node=/c/en/%s/n&rel=/r/PartOf&start=/c/en/%s&limit=5"%(word,word)
    print(url)
    obj = requests.get(url).json()

    for edge in obj['edges']:
        link = edge['end']['term'] 

        url2 = "http://api.conceptnet.io/query?node=%s&rel=/r/PartOf&end=%s&limit=10"%(link,link)
        print(url2)
        obj2 = requests.get(url2).json()
        for edge in obj2['edges']:
            word2 = edge['start']['label']
            if word2 not in distractor_list and original_word.lower() not in word2.lower():
                distractor_list.append(word2)
                   
    return distractor_list

print(len(keyword_sentence_mapping))
key_distractor_list = {}

for keyword in keyword_sentence_mapping:
    print('----------------')
    print(keyword)
    wordsense = get_wordsense(keyword_sentence_mapping[keyword][0],keyword)

    if wordsense:
        distractors = get_distractors_wordnet(wordsense,keyword)
        print(distractors)
        if len(distractors) ==0:
            distractors = get_distractors_conceptnet(keyword)
        if len(distractors) != 0:
            key_distractor_list[keyword] = distractors
    else:
#         try:
#             distractors = sense2vec_get_words(keyword,s2v)
#         except:
#             distractors=[]
        distractors = get_distractors_conceptnet(keyword)
        print(distractors)
        if len(distractors) != 0:
            key_distractor_list[keyword] = distractors

index = 1
#print ("#############################################################################")
#print ("NOTE::::::::  Since the algorithm might have errors along the way, wrong answer choices generated might not be correct for some questions. ")
#print ("#############################################################################\n\n")

qas = []##object list
print(len(key_distractor_list))

for each in key_distractor_list:
    if(index <= 3):
        sentence = keyword_sentence_mapping[each][0]
        pattern = re.compile(each, re.IGNORECASE)
        output = pattern.sub( " _______ ", sentence)
        print ("%s)"%(index),output)
        choices = [each.capitalize()] + key_distractor_list[each]
        top4choices = choices[:4]
        random.shuffle(top4choices)
        optionchoices = ['a','b','c','d']
        choices = []
        for idx,choice in enumerate(top4choices):
            #print ("\t",optionchoices[idx],")"," ",choice)
            choices.append(choice)
        #print ("\nMore options: ", choices[4:20],"\n\n")
        #print(sentence)
        #print(each)
        qaobj = QAdata(output, choices[0], choices[1], choices[2], choices[3], each)
        qas.append(qaobj)
        index = index + 1


# In[33]:


#pip install -U wn==0.0.22


# In[34]:


for x in range(len(qas)):
  print(qas[x].question)
  print(qas[x].answer1)
  print(qas[x].answer2)
  print(qas[x].answer3)
  print(qas[x].answer4)
  print('Correct : ', qas[x].correctanswer)
  print('----------------------')


# In[ ]:





# In[4]:


#pip install sense2vec


# In[2]:


# wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
# tar -xvf  s2v_reddit_2015_md.tar.gz


# In[23]:


# from sense2vec import Sense2Vec
# s2v = Sense2Vec().from_disk('s2v_old')


# In[24]:





# In[ ]:




