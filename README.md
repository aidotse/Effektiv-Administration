# Effektiv Administration

## Project description
Utveckla en MVP för en informationshanteringsapplikation avsedd för svenska myndigheter, med syftet att nyttja kraften hos språkmodeller för hantering av ostrukturerad data. Applikationen är intuitivt konstruerad för enkel uppladdning och hämtning av sådan data, och är skräddarsydd för en bred implementering över diverse organisatoriska miljöer.

<img src="files/images/prel_arch.png">

## Kravspecifikation
Konvertering av Naturligt Språk till Sökvektor
Beskrivning: Systemet ska omvandla e-postmeddelanden skrivna i naturligt språk till sökbara nyckelord/fraser för att söka i tillhörande dokumentation.

### Svarstid
Beskrivning: Efter att ett mejl har skickats av en användare ska svaret genereras och returneras inom 30 sekunder.

### Källhänvisningar
Beskrivning: Svaret ska innehålla klickbara länkar till de källor som användes för att generera svaret, vilket möjliggör för användaren att granska originalmaterialet.

### Minimal hallucination
Beskrivning: Systemet ska endast svara med exakt dokumentationsinnehåll och undvika missvisande svar. Vid ingen träff bör svaret vara "Materialet kunde inte hittas inom referensmaterialet."

### On-Premise Lösning
Beskrivning: Systemet ska installeras och köras internt (on-premise). Ingen användardata får överföras utanför systemets gränser.

### Modulär Arkitektur
Beskrivning: Systemets komponenter ska vara fristående och kommunicera via API-anrop.

### Naturligt Språk
Beskrivning: Användare ska kunna interagera med systemet via e-post i naturligt språk, även för större textmassor.

### Dokumentuppladdning (Utan förberedelser)
Beskrivning: Dataägare ska ha möjlighet att ladda upp Word-dokument direkt, utan förhandsredigering eller annan bearbetning.

### Dokumentuppladdning (Drag och Släpp)
Beskrivning: Dataägare ska kunna dra och släppa dokument i en säkrad nätverksmapp. Endast behöriga dataägare ska ha tillgång.

### Säkerhet och Skalbarhet
Beskrivning: Med tanke på målgruppen (myndigheter) är hög säkerhet och systemets förmåga att växa (skalbarhet) primära fokusområden.

## Table of Contents
- [How to install and run the project](#install_and_run)
- [How to use the project](#use_project)
- [Acknowledgements](#acknowledgements)
- [How to contribute to the project](#contribute)

## How to install and run the project <a name="install_and_run"></a>

## How to use the project <a name="use_project"></a>
Provide instructions and examples so users/contributors can use the project

## Acknowledgements <a name="acknowledgements"></a>

## How to contribute to the project <a name="contribute"></a>
