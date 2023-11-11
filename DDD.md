# Domain Driven Design

## Opis zadania

Zamodelować aplikację bankową używając Domain Driven Design: wydzielić konteksty, zdefiniować agregaty i encje, ustalić wartości, typy i ograniczenia.

### Założenia

każda osoba może mieć tylko jedno *konto*, w ramach którego może mieć wiele *rachunków* (z oddzielnym numerem i saldem). Dla uproszczenia rozważa się tylko konta osobiste dla osób fizycznych. Konto użytkownika zawiera prawnie wymagane informacje o kliencie, takie jak dane osobowe, dane kontaktowe, adres i dokument tożsamości. Przelewy wykonywane są pomiędzy rachunkami. Dla uproszczenia, obsługiwana jest tylko jedna waluta.

## Model

### Konwencje

Skróty:
* VO - Value object
* AR - Aggregate Root

Obiekty z zaokrąglonymi rogami na diagramie to VO, obiekty z ostrymi rogami to encje lub AR. Konteksty są ograniczone ramką z przerywaną linią. Adaptery między kontekstami są oznaczone dwukierunkową, grubą strzałką. Wszystkie encje domyślnie mają identyfikatory.

Jeżeli jakaś wartość nie wymaga złożonego Value Object i nie wymaga specjalnego formatu (oznaczone gwiazdką), jej typ jest podany wewnątrz obiektu. Wykorzystane pseudo-typy:
* String - wartość tekstowa (jak String w Javie),
* Date - zawiera dzień, miesiąc, rok,
* DateTime - zawiera sekundę, minutę, godzinę, dzień, miesiąc, rok (jak Date w Javie),
* BigDecimal - wartość numeryczna o "bezpiecznej" precyzji (jak BigDecimal w Javie),
* Enum - wartość z ograniczonego, dyskretnego przedziału. Możliwe wartości zależne od kontekstu, np. płeć może być "Mężczyzna", "Kobieta" lub "Inna".

### Diagram

[](./model.svg)

### Ograniczenia

#### Zarządzanie kontem

* Konto: Aggregate Root
  * Osoba: Osoba (Encja)
    * Dane osobowe: Dane osobowe (VO)
      * Imiona: String; 1-128 liter Unicode, spacji
      * Nazwisko: String; 1-128 liter Unicode, spacji
      * PESEL: PESEL (VO)
        * Wartość: String; 11 cyfr
      * Data urodzenia: Date
      * Płeć: Enum; Mężczyzna, Kobieta lub inne
    * Dokument tożsamości: Dokument tożsamości (VO)
      * Typ dokumentu: Enum; Dowód osobisty lub Paszport
      * Numer i seria: String; 1-32 litery, cyfry ANSI, `-`, `\`, `/`
      * Data wydania: Date
      * Data ważności: Date
    * Adres zamieszkania: Adres (VO)
      * Kraj: String; 1-128 liter Unicode, spacji
      * Miejscowość: String; 1-128 liter Unicode, cyfr, spacji, `-`, `.`, `'`, `&`
      * Kod pocztowy: Kod pocztowy (VO)
        * Wartość: String; regex `[0-9]{2}-[0-9]{3}`
      * Ulica: String; 1-128 liter Unicode, cyfr, spacji, `-`, `.`, `'`, `&`
      * Numer domu: String; 1-10 liter Unicode, cyfr
      * Numer mieszkania: String; 1-10 liter Unicode, cyfr
    * Adres korespondencyjny: Adres (VO)
      * j.w.
    * Dane kontaktowe: Dane kontaktowe (VO)
      * Adres e-mail: String; 1-128 znaków ANSI, obowiązkowo (i tylko raz) `@`, co najmniej jeden znak przed i po `@` - [pełna walidacja jest bardzo ciężka](https://en.wikipedia.org/wiki/Email_address#Examples)
      * Numer telefonu: String; 11 cyfr
  * Rachunki: Rachunek (Encja); dopuszczalne wiele
    * Numer rachunku: Numer rachunku (VO)
      * Wartość: String; 26 cyfr
    * Typ rachunku: Enum
    * Nazwa: String; 1-128 znaków
    * Saldo: BigDecimal
    * Operacje zaplanowane: BigDecimal

#### Transakcje

* Przelew: Aggregate Root
  * Tytuł: String; 1-64 litery Unicode, cyfry, spacja, `-`, `\`, `/`, `.`
  * Nadawca: Konto (Encja)
    * Osoba: Osoba (Encja)
      * Dane osobowe: Dane osobowe (VO)
        * Imiona: String; 1-128 liter Unicode, spacji
        * Nazwisko: String; 1-128 liter Unicode, spacji
      * Adres zamieszkania: Adres zamieszkania (VO)
        * Kraj: String; 1-128 liter Unicode, spacji
        * Miejscowość: String; 1-128 liter Unicode, cyfr, spacji, `-`, `.`, `'`, `&`
        * Kod pocztowy: Kod pocztowy (VO)
          * Wartość: String; regex `[0-9]{2}-[0-9]{3}`
        * Ulica: String; 1-128 liter Unicode, cyfr, spacji, `-`, `.`, `'`, `&`
        * Numer domu: String; 1-10 liter Unicode, cyfr
        * Numer mieszkania: String; 1-10 liter Unicode, cyfr
    * Rachunek do przelewu: Rachunek (Encja)
      * Numer rachunku: Numer rachunku (VO)
        * Wartość: String; 26 cyfr
  * Obiorca: Konto (Encja)
    * j.w.
  * Kwota: BigDecimal
  * Data zlecenia: DateTime
  * Data planowanej realizacji: DateTime; komentarz - dla przelewów okresowych i planowanych
  * Data realizacji: DateTime
  * Typ przelewu: Enum; Wewnętrzny, Zewnętrzny, Zagraniczny
