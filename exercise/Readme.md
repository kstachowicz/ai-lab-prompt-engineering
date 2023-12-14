# Ćwiczenia prompt engineering

W tym dokumencie znajdziesz kilka ćwiczeń dotyczących ćwiczenia inżynierii podpowiedzi. W tym celu podamy Ci zadanie do wykonania (np. tekst) i oczekiwane zakończenie. Twoim celem jest wymyślenie promptu, który wygeneruje pożądane zakończenie.

## Zadanie 01 – Proste zadanie

**Oto przykładowe zdanie:**

_Cieszyłem się słońcem, ale wtedy nadeszła ogromna chmura i zakryła niebo.

**Teraz wymyśl cztery indywidualne prompty, które generują następujące uzupełnienia:**

*I was enjoying the sun, but then a huge cloud came and covered the sky.*
*Ich genoss die Sonne, aber dann kam eine riesige Wolke und bedeckte den Himmel.
I was not enjoying the sun, and then a huge cloud did not come and cover the sky.
She was enjoying the sun, but then a huge cloud came and covered the sky.*

**Podsumowanie e-mail:**

Twój własny długi wątek e-mail

Teraz wymyśl prompt, który generuje następujące podsumowanie:

  

Podsumowanie: XYZ  
Pytania otwarte: XYZ  
Czynności do wykonania: XYZ

Summary: XYZ  
Open Questions: XYZ  
Action Items: XYZ

  

## Zadanie 02 - Wiele zadań w jednym prompt

Użyj tego samego przykładowego zdania:

*Cieszyłem się słońcem, ale wtedy nadeszła ogromna chmura i zakryła niebo.*

Wymyśl prompt, który generuje następujące uzupełnienie:

{    "translated-en": " I was enjoying the sun, but then a huge cloud came and covered the sky.",  
    "translated-de": "Ich genoss die Sonne, aber dann kam eine riesige Wolke und bedeckte den Himmel.",  
    "negated": "I was not enjoying the sun, and no huge cloud came and covered the sky.",  
    "third_person": "She was enjoying the sun, but then a huge cloud came and covered the sky."  
}

  

 

## Zadanie 03 - Analiza wiadomości e-mail do działu obsługi klienta

Oto e-mail od klienta:

*Cześć,  
nazywam się Mateo Gomez. Zgubiłem kartę kredytową 17 sierpnia i chciałbym poprosić o jej anulowanie. Ostatnim zakupem, jakiego dokonałem, było danie z kurczaka parmigiana w restauracji Contoso, położonej w pobliżu Hollywood Museum, za 40 USD.*

*Poniżej znajdują się moje dane osobowe do walidacji:  
Zawód: Księgowy  
Numer ubezpieczenia społecznego to 123-45-6789  
Data urodzenia: 9-9-1989  
Numer telefonu: 949-555-0110  
Adres prywatny: 1234 Hollywood Boulevard Los Angeles CA  
Połączone konto e-mail: mateo@contosorestaurant.com  
Kod Swift: CHASUS33XXX*

Wymyśl propmt, który generuje następujące dane wyjściowe:

{ "reason": "Lost Card",  
 "classified_reason": "lost_card",  
 "name": "Mateo Gomez",  
 "ssn": "123-45-6789",  
 "dob": "09/09/1989"  
}

## Zadanie 04 – Napisz prompt tworzący opis ubrania

Wymyśl propmt, który generuje krótki, dwuzdaniowy opis artykułów odzieżowych na podstawie metadanych. Oto przykładowe metadane dla artykułu:

*Pora roku: Zima  
Styl: Sweter  
Płeć: Kobieta  
Grupa docelowa: Nastolatek  
Materiał: Bawełna*

## Zadanie 05 - Napisz wpis na blogu

Napisz post na blogu na wybrany przez siebie temat.

## Zadanie 06 – Przygotuj kampanię marketingową dla wpisu na blogu

Wybierz dowolny artykuł ze strony [https://www.poznan.pl/](https://www.poznan.pl/). Na podstawie artykułu napisz prompty w celu:

·        Utworzenia listy słów kluczowych

·        Przygotowania krótkiego posta na X

·        Przygotowania dłuższego posta na Facebook

o   Przygotuj wersje dla każdej generacji: (Baby Boomer, Gen X, Millenials, Gen Y)

·        Przygotowania dłuższego posta na LinkedIn

·        Przygotowania kampanii reklamowej przesyłanej przez email
