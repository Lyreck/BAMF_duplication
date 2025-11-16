# For some interesting debates on small model choice: https://huggingface.co/openai/gpt-oss-20b/discussions/14

from ollama import chat
from ollama import ChatResponse

def generate(prompt, model='mistral-small3.2'): #check that this model is ok for the languages we're considering ?
    response = chat(model=model, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    return response.message.content


def create_prompt(text, language):

    # TODO set system prompt ?

    prompt = f"""
    You are an expert name and surname transliterator. Your task is to transliterate names from their original script ({language}) to Latin script.
    Your sole output will be a single string, which is the transliterated version of the input name.

    The input is: {text}.
    """

    # Prompt with lists: 
    # You will be given a list of names and a list of surnames in {language} script. For each input, provide its transliteration
    # Your output should by a simple dictionary with three keys: 'language' (with valuealways set to {language})'name_transliteration' and 'surname_transliteration',  and their corresponding values.
    # Here is the name list: {names}

    # -----
    # Here is the surname list: {surnames}

    return prompt

def create_prompt_list(texts, language): #TODO: create a max context window limit to divide prompts in order to make sure the list of names to transliterate is not too long.
    
    # TODO set system prompt ?

    prompt = f"""
    You are an expert name and surname transliterator. Your task is to transliterate names from their original script ({language}) to Latin script.
    You will be given a list of names and a list of surnames in {language} script.
    Your sole output shold be a list of strings, each being the transliterated version of the corresponding input name.

    The input is: {texts}.

    Now provide the transliteration 
    """

    return prompt

def run_llm(text, language="ukrainian", model="mistral-small3.2"):

    if text is str:
        prompt = create_prompt(text, language)
    else: 
        prompt = create_prompt_list(text, language)

    print(prompt)

    response = generate(prompt, model=model)

    return response

if __name__ == "__main__":
    sample_text = "Іваненко"
    language = "ukrainian"
    model = "mistral-small3.2"

    import time as t

    t0 = t.time()
    # for i in range(1000):
    #     transliteration = run_llm(sample_text, language, model) # 140 secondes pour 1000 itérations.
    sample_texts=[
    "Августа", "Густа",
    "Аврелія", "Аурелія", "Аурика",
    "Агафія", "Агапія", "Гафія", "Гапка",
    "Агата", "Аґата",
    "Аглая", "Аглаїда",
    "Агнеса", "Агнія", "Агна",
    "Агрипина", "Горпина", "Груня",
    "Аделаїда", "Аделіна", "Аделя", "Адиля", "Адель",
    "Адріана", "Андріана", "Адріанна",
    "Акилина", "Килина", "Кулина", "Якилина",
    "Алевтина", "Ала", "Аля", "Тіна",
    "Аліна", "Ліна",
    "Альбертина", "Альбертіна",
    "Альбіна", "Альвіна",
    "Анастасія", "Настасія", "Настя", "Наста", "Настка",
    "Анатолія", "Анатоля",
    "Ангеліна", "Ангела",
    "Анжела", "Ангела",
    "Анжеліка", "Ангеліка", "Анжеліна",
    "Анна", "Ганна", "Анничка", "Анка", "Аня",
    "Антонида", "Антоніда",
    "Антоніна", "Тоня", "Антонія",
    "Анфіса", "Анфиса",
    "Арсена", "Арсенія",
    "Артемізія", "Артемісія", "Артеміса", "Артеміза", "Артемія",
    "Аскліпія", "Асклепія",
    "Аурика", "Аурелія", "Аврелія",
    "Афіна", "Атена",
    "Афродіта", "Афродита",
    "Божена", "Бажана",
    "Беатриса", "Беата",
    "Богдана", "Дана",
    "Богуслава", "Слава",
    "Болеслава", "Борислава", "Броніслава",
    "Валерія", "Лера", "Лєра", "Леруня", "Леруся", "Леруша", "Лерочка",
    "Варвара", "Барбара",
    "Векла", "Фекла", "Текля",
    "Вікторина", "Вікторія", "Віка",
    "Вілена", "Олена",
    "Віола", "Віоланта",
    "Віолетта", "Віола",
    "Віта", "Віталія", "Віталіна",
    "Влада", "Владислава", "Слава", "Володимира",
    "Всеслава", "В'ячеслава", "Вячеслава",
    "Галина", "Галка", "Галя",
    "Ганна", "Анна",
    "Гафія", "Агафія",
    "Гелена", "Гелина",
    "Гертруда", "Герта", "Ґертруда",
    "Глафіра", "Глафира", "Глафа", "Фіра",
    "Гликерія", "Ликерія", "Ликера", "Лукера",
    "Горпина", "Агриппина", "Аґриппина",
    "Густава", "Густа", "Ґустава",
    "Дана", "Даня", "Даніелла", "Данієлла",
    "Дарина", "Одарина", "Одарка", "Даріня",
    "Дарія", "Одарка", "Дарина", "Дарка", "Дарья", "Дар'я",
    "Дзвенислава", "Дзвінка", "Звенислава",
    "Діана", "Діна",
    "Домаха", "Домна",
    "Дорофея", "Доротея", "Дорофія",
    "Евеліна", "Евелина",
    "Едіта", "Едита",
    "Ельвіна", "Альбіна", "Ельвіра",
    "Емма", "Еммануїла", "Еммануель", "Еммануела",
    "Емілія", "Еміля",
    "Есфір", "Естер", "Фіра",
    "Єва", "Євгенія", "Євгена", "Югина", "Ївга",
    "Євдокія", "Докія", "Явдоха",
    "Євфросинія", "Єфросинія", "Фросина", "Фрося",
    "Єлизавета", "Лизавета", "Лисавета", "Гальшка", "Галшка", "Ліза",
    "Єпистимія", "Єпистима", "Пистина",
    "Жадана", "Ждана",
    "Жанна", "Іоанна", "Іванна", "Іванка",
    "Жозефіна", "Жозефа",
    "Зірка", "Зіра",
    "Зореслава", "Зоряна", "Зоря", "Зоя",
    "Ореста",
    "Орина",
    "Орися", "Оришка",
    "Павла", "Пава",
    "Павлина", "Павла", "Пава",
    "Пелагія", "Пелагея", "Палагна", "Палазга", "Палажка", "Пазина",
    "Параскева", "Параскевія", "Парасковія", "Параска",
    "Поліна", "Павлина", "Аполлінарія", "Паулина",
    "Пріська", "Єфросинія",
    "Пульхерія", "Пульхера",
    "Радомира", "Радимира",
    "Раїса", "Рая",
    "Ракель", "Рахіль", "Рахель", "Рошель",
    "Ревека", "Ребекка",
    "Ріана", "Ріанна",
    "Рогволода",
    "Рогнеда", "Рогніда",
    "Роза", "Рузина",
    "Розалія", "Рузалія",
    "Роксана", "Роксолана",
    "Романа", "Романна", "Романія",
    "Русудан", "Русудана",
    "Рут", "Руф", "Руфа",
    "Руфина", "Рутина", "Руфіна", "Руфіма",
    "Сара", "Сарра",
    "Світлана", "Лана",
    "Світозара", "Світояра",
    "Святогора", "Святослава",
    "Секлета", "Секлетина",
    "Симона", "Сімона",
    "Соломія", "Саломея",
    "Софія", "Зофія", "Соня", "Софья", "Соф'я",
    "Станіслава", "Стася", "Станя",
    "Стелла", "Ела",
    "Стефанія", "Стефанида",
    "Сусанна", "Сусана", "Сосанна", "Зузана", "Сюзанна",
    "Судислава",
    "Таїсія", "Таїса",
    "Тамара", "Тамар",
    "Текля", "Текла", "Фекла",
    "Тереза",
    "Тетяна", "Таня", "Тетьяна", "Тет'яна",
    "Тіна",
    "Трояна",
    "Устина", "Юстина",
    "Уляна", "Ул'яна",
    "Фаїна",
    "Февронія", "Февросія", "Хівря",
    "Феліція", "Фелікса",
    "Филіцата", "Филікитата", "Филіцитата",
    "Феодора", "Федора", "Тодора",
    "Феодосія", "Федосія", "Теодозія",
    "Фотина", "Фотинія", "Хотина",
    "Харитина", "Харитя", "Харита",
    "Хрися", "Хриса",
    "Христина", "Христя",
    "Цецилія", "Кекилія",
    "Цвітана", "Цветана",
    "Юдита", "Юдита", "Юдиф", "Юдихва",
    "Юзефа", "Юзепа", "Йосипа", "Осипа",
    "Юлія", "Юлина",
    "Юліана", "Юліанна", "Юліанія",
    "Юнія", "Юна",
    "Юстина", "Устина",
    "Юхимія", "Юхимина", "Юхима", "Хима",
    "Явдоха", "Євдокія",
    "Яна", "Іванна", "Янка", "Яніна",
    "Яромира", "Яра"
]

    transliteration = run_llm(sample_texts, language, model) # 80 seconds for 394 iterations.
    # So it seems better timewise to have a one by one approach. Check that
    # quality is ok too, but I think it'll be better for the context window to have 
    # small prompts.

    print(f"Time taken for {len(sample_texts)} iterations with list approach: {t.time() - t0} seconds")
    print(f"Transliteration of '{sample_text}' in {language}: {transliteration}")




    # ['Avhusta', 'Husta', 'Avreliia', 'Aureliia', 'Aurika', 'Ahapia', 'Ahapia', 'Hafia', 'Hapka', 'Ahata', 'Aґata', 'Ahlaia', 'Ahlaїda', 'Ahnesa', 'Ahniia', 'Ahna', 'Ahrypyna', 'Horypyna', 'Hrunia', 'Adelaїda', 'Adelina', 'Adelia', 'Adyla', 'Adel', 'Adriana', 'Andriana', 'Adrianna', 'Akylina', 'Kylina', 'Kulina', 'Yakylina', 'Alevtyna', 'Ala', 'Alia', 'Tina', 'Alina', 'Lina', 'Albertyna', 'Albertyna', 'Albyna', 'Alvyna', 'Anastasiia', 'Nastasiia', 'Nastia', 'Nasta', 'Nastka', 'Anatoliia', 'Anatolia', 'Anhelina', 'Anhela', 'Anhela', 'Anhela', 'Anhelika', 'Anhelika', 'Anhelina', 'Anna', 'Hanna', 'Annychka', 'Anka', 'Ania', 'Antonida', 'Antonida', 'Antonina', 'Tonia', 'Antonia', 'Anfisa', 'Anfysa', 'Arsena', 'Arseniia', 'Artemiziia', 'Artemisiia', 'Artemisa', 'Artemiza', 'Artemiia', 'Asklipiia', 'Asklepiia', 'Aurika', 'Aureliia', 'Avreliia', 'Afina', 'Atena', 'Afrodita', 'Afrodita', 'Bozhena', 'Bazhana', 'Beatrixa', 'Beata', 'Bohdana', 'Dana', 'Bohuslava', 'Slava', 'Boleslava', 'Boryslava', 'Bronislava', 'Valeriia', 'Lera', 'Lera', 'Lerunia', 'Lerusia', 'Lerusha', 'Lerochka', 'Varvara', 'Barbara', 'Vekla', 'Fekla', 'Teklia', 'Viktorina', 'Viktoriia', 'Vika', 'Vilena', 'Olena', 'Viola', 'Violanta', 'Violetta', 'Viola', 'Vita', 'Vitaliia', 'Vitalina', 'Vlada', 'Vladyslava', 'Slava', 'Volodymyra', 'Vseslava', 'Vyacheslava', 'Vyacheslava', 'Halyna', 'Halka', 'Halia', 'Hanna', 'Anna', 'Hafia', 'Ahapia', 'Helena', 'Helina', 'Hertruda', 'Herta', 'Ґertruda', 'Hlafyra', 'Hlafyra', 'Hlafia', 'Fira', 'Hlykeriia', 'Lykeriia', 'Lykeria', 'Lukera', 'Horypyna', 'Ahrypyna', 'Aґrypyna', 'Hustava', 'Husta', 'Ґustava', 'Dana', 'Dania', 'Daniella', 'Daniella', 'Daryna', 'Odarina', 'Odarka', 'Darinia', 'Daria', 'Odarka', 'Daryna', 'Darka', 'Dariia', 'Daria', 'Dzvenyslava', 'Dzvinka', 'Zvenyslava', 'Diana', 'Dina', 'Domakha', 'Domna', 'Dorofeia', 'Doroteia', 'Dorofia', 'Evelina', 'Evelina', 'Edita', 'Edita', 'Elvyna', 'Albyna', 'Elvira', 'Emma', 'Emmanuїla', 'Emmanuel', 'Emmanuela', 'Emiliia', 'Emilia', 'Esfir', 'Ester', 'Fira', 'Eva', 'Yevheniia', 'Yevhena', 'Yuhyna', 'Ivha', 'Yevdokiia', 'Dokiia', 'Yavdokha', 'Yevfrosyniia', 'Yefrosyniia', 'Frosyna', 'Frosia', 'Yelizaveta', 'Lizaveta', 'Lisaveta', 'Halishka', 'Halishka', 'Liza', 'Yepystymiia', 'Yepystyma', 'Pystyna', 'Zhadana', 'Zhdana', 'Zhanna', 'Ioanna', 'Ivanna', 'Ivanka', 'Zhozefina', 'Zhozefa', 'Zirka', 'Zira', 'Zoreslava', 'Zoryana', 'Zoria', 'Zoya', 'Oresta', 'Orina', 'Orisia', 'Orishka', 'Pavla', 'Pava', 'Pavlyna', 'Pavla', 'Pava', 'Pelagiia', 'Pelageia', 'Palahna', 'Palazha', 'Palazhka', 'Pazyna', 'Paraskeva', 'Paraskeviia', 'Paraskoviia', 'Paraska', 'Polina', 'Pavlyna', 'Apollinariia', 'Paulina', 'Priska', 'Yefrosyniia', 'Pulkheriia', 'Pulkhera', 'Radomyra', 'Radymyra', 'Raїsa', 'Raia', 'Rakel', 'Rakhil', 'Rakhel', 'Roshel', 'Rebeka', 'Rebekka', 'Riia', 'Rianna', ' Rohvoloda', 'Rohneida', 'Rohniida', 'Roza', 'Ruzyna', 'Rozalia', 'Ruzalia', 'Roksana', 'Roksolana', 'Romana', 'Romanna', 'Romaniia', 'Rusudan', 'Rusudana', 'Rut', 'Ruf', 'Rufa', 'Rufyna', 'Rutyna', 'Rufyna', 'Rufima', 'Sara', 'Sarra', 'Svitlana', 'Lana', 'Svitozara', 'Sviatoiara', 'Sviatohora', 'Sviatoslava', 'Sekeleta', 'Sekeletyna', 'Simona', 'Simona', 'Solomiia', 'Salomeia', 'Sofiia', 'Zofiia', 'Sonia', 'Sofiia', 'Sofia', 'Stanislava', 'Stasia', 'Stania', 'Stella', 'Ela', 'Stefaniia', 'Stefanyda', 'Susanna', 'Susana', 'Sosanna', 'Zuzana', 'Suzanna', 'Sudyslava', 'Taїsiia', 'Taїsa', 'Tamara', 'Tamara', 'Teklia', 'Tekla', 'Fekla', 'Tereza', 'Tetiana', 'Tania', 'Tetiana', 'Tetiana', 'Tina', 'Troiana', 'Ustyna', 'Iustyna', 'Uliana', 'Uliana', 'Faїna', 'Fevroniia', 'Fevrosiia', 'Khivria', 'Felitsiia', 'Feliksa', 'Fylitsata', 'Fylikitata', 'Fylitsitata', 'Feodora', 'Fedora', 'Todora', 'Feodosia', 'Fedosiia', 'Teodosiia', 'Fotyna', 'Fotiniia', 'Khotyna', 'Kharytyna', 'Kharytia', 'Kharyta', 'Khrysia', 'Khrysa', 'Khrystyna', 'Khrystia', 'Tsetsiia', 'Kekiliia', 'Tsvitana', 'Tsvetana', 'Iudita', 'Iudita', 'Iudif', 'Iudikhva', 'Iuzefa', 'Iuzefa', 'Iosyfa', 'Osyfa', 'Iuliia', 'Iulina', 'Iuliiana', 'Iuliianna', 'Iuliianiia', 'Iuniia', 'Iuna', 'Iustyna', 'Ustyna', 'Iukhymiia', 'Iukhymina', 'Iukhyma', 'Khymia', 'Iavdokha', 'Yevdokiia', 'Iana', 'Ivanna', 'Ianka', 'Ianina', 'Iaromyra', 'Iara']