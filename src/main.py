""" Main module to start the application """
import sys

from model_wrapper.model_wrapper import prompt

def main() -> None:
    """ For now just a dummy """

    system_message = """
Du är nu en chatbot för vårdspersonal vars mål är att ta ut relevant data ur databasen och svara på frågor. Se till att ge ett tydligt svar på frågan. Om du hittar svaret i en fil måste du refferera till exakt vart du hittade det (filnamn, datum).
Fråga:
Följande är data från databasen:
 
2021-05-12.txt:{
Datum: 2021-05-12
Läkarbesök: Kirurgkliniken
Anteckningar: Niels presenterade med svullnad och rodnad kring höger knä. Inga tecken på infektion vid blodprov. Möjligt överansträngning eller mindre skada på ligament. Rekommenderad vila och is.
}
LäkarbesökVästerås.txt:{
Datum: 2021-10-03
Läkarbesök: Allmänpraktiken
Anteckningar: Eftersom för uppföljning av knäskada. Bättre rörlighet och mindre smärta. Diskuterade fysioterapi som nästa steg för rehabilitering.
}
17563.txt:{
Datum: 2022-02-21
Läkarbesök: Kardiologkliniken
Anteckningar: Niels upplevde lätt andfåddhet vid ansträngning. EKG och ekokardiogram visade inga avvikelser. Råddes att minska på koffeinintaget och öka fysisk aktivitet.
}

Ditt svar är:
    """
    messages = ["Har Niels någon historik av högt koffeinintag och har han haft några infekt"]

    # model.query(system_message=system_message, user_messages=messages)
    print(prompt(system_message, messages))
    return 0




if __name__ == '__main__':
    sys.exit(main())
