""" Main module to start the application """
import sys

from model_wrapper import prompt_model
from query_wrapper import preform_query
from test_prompts.test_prompts import test_prompts

chunks = """---
Title: Projektplan_-_Helhälsa.docx
Page: 0
Section: 1
Content:
 Mäts genom juridisk granskning och säkerhetstester.Omfattning:Detaljerad beskrivning av projektets omfattning inkluderar utveckling av mobilapplikationen, integration med wearables och andra appar, backend-utveckling, skapande av dashboards och rapporteringsfunktioner, samt marknadsföring och lansering. Projektet inkluderar inte kontinuerligt underhåll och support eller utveckling av hårdvara.Tidsplan:Här är huvudpunkterna från projektets tidsplan:Projektstart: 1 januari 2024Designfas: 1 januari - 28 februari 2024Utvecklingsfas: 1 mars - 31 augusti 2024Testningsfas: 1 september - 31 oktober 2024Lanseringsfas: 1 november - 31 december 2024Budget:Detaljerad budget inklusive allokering av resurser:Personal: 1 miljon SEKUtrustning och Verktyg: 300,000 SEKLicenser: 200,000 SEKMarknadsföring: 400,000 SEKÖvriga kostnader: 100,000 SEKTotal budget: 2 miljoner SEKKvalitetskrav:
---
---
Title: Projektplan_-_Helhälsa.docx
Page: 0
Section: 0
Content:
 Projektplan för HelHälsa Mobilapplikation:Introduktion:Projektplanen för HelHälsa Mobilapplikation syftar till att ge en detaljerad översikt över hur projektet ska genomföras för att uppfylla de fastställda målen. Dokumentet omfattar projektets mål, omfattning, tidsplan, budget, kvalitetskrav, riskhantering och kommunikationsplan.Mål:Utöver de övergripande målen som beskrivs i projektdirektivet, här är några detaljerade mål och hur de ska mätas:Användarvänlighet:Målet är att 90% av testanvändarna ska kunna navigera applikationen utan hjälp.Mäts genom användartester och feedback.Integration:Målet är att stödja minst 10 olika wearables och hälsorelaterade appar vid lansering.Mäts genom integrationstester.Datasekretess:Målet är att uppnå fullständig överensstämmelse med GDPR och andra relevanta dataskyddslagar.Mäts genom juridisk granskning och säkerhetstester.Omfattning:
---
---
Title: Projektplan_-_Helhälsa.docx
Page: 0
Section: 3
Content:
 Planering: Identifiering, bedömning, och hantering av risker genom regelbunden översyn och förberedande åtgärder.Kommunikationsplan:Teamkommunikation: Veckovisa möten och dagliga stand-ups för att diskutera framsteg och eventuella problem.Stakeholderkommunikation: Månadsvisa uppdateringar och kvartalsvisa genomgångar för att informera intressenter om projektets framsteg.Kris kommunikation: Etablerade protokoll för att kommunicera och hantera eventuella kriser eller stora problem som uppstår under projektet.Denna projektplan ger en omfattande översikt över hur projektet ska genomföras för att säkerställa framgångsrik utveckling och lansering av HelHälsa mobilapplikationen.
---
---
Title: Projektplan_-_Helhälsa.docx
Page: 0
Section: 2
Content:
 Licenser: 200,000 SEKMarknadsföring: 400,000 SEKÖvriga kostnader: 100,000 SEKTotal budget: 2 miljoner SEKKvalitetskrav:Prestanda: Applikationen ska ladda inom 2 sekunder och svarstiden för användarinteraktioner ska vara under 1 sekund.Säkerhet: Applikationen ska uppfylla alla relevanta säkerhetsstandarder inklusive GDPR.Användarvänlighet: Applikationen ska vara intuitiv och enkel att använda, med en hög nivå av användartillfredsställelse.Riskhantering:Tekniska Risker: Såsom buggar, fel i tredjepartsintegrationer och hårdvaruproblem.Säkerhetsrisker: Såsom dataintrång och förlust av användardata.Juridiska Risker: Såsom överensstämmelse med dataskyddslagar och andra relevanta regelverk.Planering: Identifiering, bedömning, och hantering av risker genom regelbunden översyn och förberedande åtgärder.Kommunikationsplan:"""

def question_loop():
    while True:
        usr_prompt = input("Ställ din fråga: ")
        if usr_prompt == "e":
            break
        query_string = usr_prompt
        result = preform_query(query_string)
        # print("results:")
        # print(str(result))

        prompt_model(str(result), usr_prompt)


def main() -> None:
    """ For now just a dummy """

    sys_prompt = test_prompts[0]["sys_prompt"]
    usr_prompt = test_prompts[0]["usr_prompt"]
    # prompt_model(sys_prompt, usr_prompt)
    prompt_model(chunks, "Kan du sammanfatta projektplanen för Helhälsa Mobilapplikation?")


    # query_string = usr_prompt
    # result = preform_query(query_string)
    # print("results:")
    # print(str(result))

    # prompt_model(str(result), usr_prompt)

    question_loop()

    return 0


# could create user interface in json file that can be edited...

if __name__ == '__main__':
    sys.exit(main())

#     system_message = """
# Du är nu en chatbot för vårdspersonal vars mål är att ta ut relevant data ur databasen och svara på frågor. Se till att ge ett tydligt svar på frågan. Om du hittar svaret i en fil måste du refferera till exakt vart du hittade det (filnamn, datum).
# Fråga:
# Följande är data från databasen:
 
# 2021-05-12.txt:{
# Datum: 2021-05-12
# Läkarbesök: Kirurgkliniken
# Anteckningar: Niels presenterade med svullnad och rodnad kring höger knä. Inga tecken på infektion vid blodprov. Möjligt överansträngning eller mindre skada på ligament. Rekommenderad vila och is.
# }
# LäkarbesökVästerås.txt:{
# Datum: 2021-10-03
# Läkarbesök: Allmänpraktiken
# Anteckningar: Eftersom för uppföljning av knäskada. Bättre rörlighet och mindre smärta. Diskuterade fysioterapi som nästa steg för rehabilitering.
# }
# 17563.txt:{
# Datum: 2022-02-21
# Läkarbesök: Kardiologkliniken
# Anteckningar: Niels upplevde lätt andfåddhet vid ansträngning. EKG och ekokardiogram visade inga avvikelser. Råddes att minska på koffeinintaget och öka fysisk aktivitet.
# }

# Ditt svar är:
#     """
#     messages = ["Har Niels någon historik av högt koffeinintag och har han haft några infekt"]