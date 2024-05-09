class Chess():
    sort='thought provoking game'
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def move(self):
        return f'{self.name} {self.color} rengli fiqurların üzvüdür. {self.name} fiquru fikirləşilərək irəli və geri həmlələrlə istifadə olunur.'
    def rank(self):
        
        return f'{self.name} fiquru {self.color} renglilerin uzvudur ve {self.color} kamandasinin qazanmasi ucun calisir.'
    def place(self):
        return f'{self.name} fiquru şahmat taxtasının {self.color} kamandası arasında yerləşir. '



class King(Chess):
    __info='Zəfər inanan və bunun uğrunda savaşanlarındır . . .'
    def move(self):
        return f'{self.name} kralı hər istiqamətdə 1 xana ilə hərəkət edə bilər. ' 

    def rank(self):
        write=self.__info
        return f"{self.name} {self.color}  kamandasının lideridir. O vardırsa heç kimin olmamağı önəmli deyil. O yoxdursa heç kimin olmağı önəmli deyil . {write}"    
    def place(self):
        if self.color.lower()=='ag' or self.color.lower()=='white':
            return f"{self.name} {self.color}  kamandasında olduğu üçün  oyun başladıqda  'e1' xanasında yerləşir .Əks rəng olan 'Qara' rengde yerlesir."
        elif self.color.lower()=='qara' or self.color.lower()=='black':
            return f"{self.name} {self.color}  kamandasında olduğu üçün  oyun başladıqda  'e8' xanasında yerləşir . Əks rəng olan 'Ag' rengde yerlesir."
        else :
            return f"{self.name} firuqu ancaq ag(white) ve ya qara(black) reng ola biler"
    def rokirovka(self):
            if self.color.lower()=='ag' or self.color.lower()=='white':
                return f" Şah e1-dən c1-ə hərəkət etdi. a1 topu d1-ə hərəkət etdi."
            elif self.color.lower()=='qara' or self.color.lower()=='black':
                 return f"Şah e8-dən c8-ə hərəkət etdi. a8 topu d8-ə hərəkət etdi."
            else :
                 return f"{self.name} firuqu ancaq ag(white) ve ya qara(black) reng ola biler" 

class Queen(Chess):
    def move(self):
        return f'{self.name} vəziri hər istiqamətdə istənilən xana sayı  ilə hərəkət edə bilər. ' 

    def rank(self):
        return f"{self.name} {self.color}  kamandasının önəmli fiqurlarındandır. Şahdan sonra ikinci fiqurdur."    
    def place(self):
        if self.color.lower()=='ag' or self.color.lower()=='white':
            return f"{self.name} {self.color}  kamandasında olduğu üçün  oyun başladıqda  'd1' xanasında yerləşir .{(self.color).capitalize()} rəngdə olan xanada yerləşir"
        elif self.color.lower()=='qara' or self.color.lower()=='black':
            return f"{self.name} {self.color}  kamandasında olduğu üçün  oyun başladıqda  'd8' xanasında yerləşir . {(self.color).capitalize()} rəngdə olan xanada yerləşir"
        else :
            return f"{self.name} firuqu ancaq ag(white) ve ya qara(black) reng ola biler"
        
class Rook(Chess):
    def move(self):
        return f'{self.name} topu üfuqi və şaquli  istiqamətdə istənilən xana sayı  ilə hərəkət edə bilər. ' 
    def rank(self):
        return f"{self.name} {self.color}  kamandasının önəmli fiqurlarındandır.Hər kamandada iki ədəd olur. Funksiyalarına görə üçüncü önəmli fiqurdur."    
    def place(self):
        if self.color.lower()=='ag' or self.color.lower()=='white':
            return f"{self.name} {self.color}  kamandasında olduğu üçün  oyun başladıqda  'a1' və 'h1' xanalarında yerləşir ."
        elif self.color.lower()=='qara' or self.color.lower()=='black':
            return f"{self.name} {self.color}  kamandasında olduğu üçün  oyun başladıqda  'a8' və 'h8' xanalarında yerləşir"
        else :
            return f"{self.name} firuqu ancaq ag(white) ve ya qara(black) reng ola biler"

class Bishop(Chess):
    def move(self):
        return f'{self.name} fili diaqonal  istiqamətdə istənilən xana sayı  ilə hərəkət edə bilər. ' 
    def rank(self):
        return f"{self.name} {self.color}  kamandasının önəmli fiqurlarındandır.Hər kamandada iki ədəd olur.  Funksiyalarına görə dördüncü önəmli fiqurdur."    
    def place(self):
        if self.color.lower()=='ag' or self.color.lower()=='white':
            return f"{self.name} {self.color}  kamandasında olduğu üçün  oyun başladıqda  'c1' və 'f1' xanalarında yerləşir ."
        elif self.color.lower()=='qara' or self.color.lower()=='black':
            return f"{self.name} {self.color}  kamandasında olduğu üçün  oyun başladıqda  'c8' və 'f8' xanalarında yerləşir"
        else :
            return f"{self.name} firuqu ancaq ag(white) ve ya qara(black) reng ola biler"
    
class Knight(Chess):
    def move(self):
        return f'{self.name} atı "L" formasında hərəkət edir: iki hüceyrə bir istiqamətdə və bir hüceyrə ona perpendikulyar istiqamətdə. Bu, ona digər fiqurların üzərindən keçmək imkanı verir. Şahmat taxtasında belə hərəkət etmə qabiliyyəti atı unikallaşdırır və mürəkkəb strategiyalar qurmaq üçün istifadə olunur. ' 
    def rank(self):
        return f"{self.name} {self.color}  kamandasının fiqurlarındandır.Mürəkkəb hərəkətləri ilə rəqibi çaşdırır.Hər kamandada iki ədəd olur.  Funksiyalarına görə beşinci önəmli fiqurdur."    
    def place(self):
        if self.color.lower()=='ag' or self.color.lower()=='white':
            return f"{self.name} {self.color}  kamandasında olduğu üçün  oyun başladıqda  'b1' və 'g1' xanalarında yerləşir ."
        elif self.color.lower()=='qara' or self.color.lower()=='black':
            return f"{self.name} {self.color}  kamandasında olduğu üçün  oyun başladıqda  'b8' və 'g8' xanalarında yerləşir"
        else :
            return f"{self.name} firuqu ancaq ag(white) ve ya qara(black) reng ola biler"    
class Pawn(Chess):
    def move(self):
        return f'{self.name} piyadası bir addım irəli hərəkət edir, lakin oyunun başlanğıcında hər bir piyada iki addım irəli hərəkət edə bilər.Piyadalar diaqonal istiqamətdə bir addım hərəkət edərək rəqib fiqurunu götürə bilər.Piyadalar son sıraya çatdıqda, onlar adətən vezir, at, fil və ya top kimi digər fiqurlara çevrilə bilər. Bu proses "təşviq" (promotion) adlanır. Piyadaların unikal hərəkət qaydalarından biri də "en passant" gedişidir ki, bu zaman piyada rəqib piyadanın yanından keçərək onu götürə bilər. ' 
    def rank(self):
        return f"{self.name} {self.color}  kamandasının fiqurlarındandır.Şahmat taxtasında ən zəif firuqdur."    
    def place(self):
        if self.color.lower()=='ag' or self.color.lower()=='white':
            return f"Ağ fiqurlar üçün {self.name} piyadalar taxtanın ikinci sırasında yerləşir. Bu sıradakı bütün xanalar ağ piyadaların başlanğıc mövqeləridir: a2, b2, c2, d2, e2, f2, g2, h2"
        elif self.color.lower()=='qara' or self.color.lower()=='black':
            return f"Qara fiqurlar üçün {self.name} piyadalar taxtanın yeddinci sırasında yerləşir. Buradakı xanalar qara piyadaların başlanğıc mövqeləridir: a7, b7, c7, d7, e7, f7, g7, h7."
        else :
            return f"{self.name} firuqu ancaq ag(white) ve ya qara(black) reng ola biler"    


def find_rank(figure):
    print(figure.rank())
def find_place(figure):
    print(figure.place())
def find_place(figure):
    print(figure.move())
   
queen=Queen('Vezir','Black')
print(queen.place())
pawn=Pawn('Pawn','qara')
find_place(pawn)
shah=King("Şah","Qara")
find_rank(shah)

    