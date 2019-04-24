import pymysql
import random

def data_generator():
    conn = pymysql.connect(host = "120.78.82.130", port = 3306, user = "root", passwd = "cuhksz", db = "AES", charset = "utf8")
    
    cursor = conn.cursor()

    current_id = 6000000000

    question = ["Reviving the practice of using elements of popular music in classical composition, an approach that had been in \n" +
    "hibernation in the United States during the 1960s, composer Philip Glass (born 1937) embraced the ethos of popular music in \n" +
    "his compositions. Glass based two symphonies on music by rock musicians David Bowie and Brian Eno, but the symphonies' sound \n" + 
    "is distinctively his. Popular elements do not appear out of place in Glass's classical music, which from its early days has \n" + 
    "shared certain harmonies and rhythms with rock music. Yet this use of popular elements has not made Glass a composer of popular \n" + 
    "music. His music is not a version of popular music packaged to attract classical listeners; it is high art for listeners steeped \n" + 
    "in rock rather than the classics. \n" + 
    "1. The passage addresses which of the following issues related to Glass's use of popular elements in his classical compositions? \n" + 
    "A. How it is regarded by listeners who prefer rock to the classics \n" + 
    "B. How it has affected the commercial success of Glass's music \n" + 
    "C. Whether it has contributed to a revival of interest among other composers in using popular elements in their compositions\n" +  
    "D. Whether it has had a detrimental effect on Glass's reputation as a composer of classical music \n" + 
    "E. Whether it has caused certain of Glass's works to be derivative in quality \n" + 
    "Consider each of the three choices separately and select all that apply. \n" +
    "2. The passage suggests that Glass's work displays which of the following qualities?\n" + 
    "A. A return to the use of popular music in classical compositions \n" +
    "B. An attempt to elevate rock music to an artistic status more closely approximating that of classical music \n" +  
    "C. A long-standing tendency to incorporate elements from two apparently disparate musical styles \n",
    
    "In parts of the Arctic, the land grades into the landfast ice so _______ that you can walk off the coast and not know you are over the hidden sea. \n" +  
    "(A) permanently \n" + 
    "(B) imperceptibly \n" +
    "(C) irregularly \n" + 
    "(D) precariously \n" + 
    "(E) slightly \n",

    "It is refreshing to read a book about our planet by an author who does not allow facts to be (i)__________ by politics: well aware of the political disputes about the effects of human activities on climate and biodiversity, this author does not permit them to (ii)__________ his comprehensive description of what we know about our biosphere. He emphasizes the enormous gaps in our knowledge, the sparseness of our observations, and the (iii)__________, calling attention to the many aspects of planetary evolution that must be better understood before we can accurately diagnose the condition of our planet. \n" +
    "(A)overshadowed    (B)invalidated   (C)illuminated    (D)enhance    (E)obscure \n" + 
    "(F)underscore      (G)plausibility of our hypotheses  (H)certainty of our entitlement (I)superficiality of our theories \n",
    
    "Claim: Governments must ensure that their major cities receive the financial support they need in order to thrive. \n" + 
    "Reason: It is primarily in cities that a nation's cultural traditions are preserved and generated. \n" + 
    "Write a response in which you discuss the extent to which you agree or disagree with the claim and the reason on which that claim is based. \n",
    
    "Eight hundroid insects were weighed, and the resulting measurements, in milligrams, are summearized in the boxplot below \n" + 
    "(a)What are the range, the three quartiles, and the interquartile range of the measurements? \n" + 
    "(b)If the 80th percentile range of the measurements is 130 milligrams, about how many measurements are between 126 milligrams and 130 milligrams? \n"]

    question_type = ["Verbal Reasoning", "Multiple Choice", "Text Completion", "Issue", "Mathematical Analysis"]

    answers = ["E \n AC\n", "B", "AEI", "nothing", "blah"]

    analysis = ["nothing", "nothing", "nothing", "issue essay to write", "blah"]

    for i in range(len(question)):
        random_diff = random.randint(1, 10)
        effect_row = cursor.execute('insert into question_base values("{}", "{}", {}, "{}", "{}", "{}");'.format(str(current_id), analysis[i], random_diff, question[i], answers[i], question_type[i]))
        current_id += 1
        
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    data_generator()   
