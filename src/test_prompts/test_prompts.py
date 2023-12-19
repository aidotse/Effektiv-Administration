test_prompts = [
    {
        "sys_prompt": "[{'filepath': './documents2/Projektdirektiv_-_Helhälsa.docx', 'text': 'Budget:\n\nÖversiktlig budget för projektet är uppskattad till 2 miljoner SEK, som\nomfattar personal, utvecklingsverktyg, licenser, marknadsföring och\nandra relaterade kostnader. Tidsram:\n\nProjektets startdatum är planerat till den 1 januari 2024 och slutdatum\när planerat till den 31 december 2024.'}, {'filepath': './documents2/Budget_-_Helhälsa.docx', 'text': 'Den totala budgeten för projektet\när uppskattad till 2 miljoner SEK och sträcker sig från projektets\nstartdatum den 1 januari 2024 till slutdatum den 31 december 2024. Personal:\n\n-  **Projektledare:** 200,000 SEK\n\n-  **Utvecklingsteam:** 500,000 SEK\n\n   -  Inkluderar löner för utvecklare, designers, och testare. -  **Marknadsföringsteam:** 100,000 SEK\n\n-  **Övrig personal (administrativ personal, IT-support, etc.'}, {'filepath': './documents2/Projektplan_-_Helhälsa.docx', 'text': 'Tidsplan:\n\nHär är huvudpunkterna från projektets tidsplan:\n\n-  **Projektstart:** 1 januari 2024\n\n-  **Designfas:** 1 januari - 28 februari 2024\n\n-  **Utvecklingsfas:** 1 mars - 31 augusti 2024\n\n-  **Testningsfas:** 1 september - 31 oktober 2024\n\n-  **Lanseringsfas:** 1 november - 31 december 2024\n\nBudget:\n\nDetaljerad budget inklusive allokering av resurser:\n\n-  **Personal:** 1 miljon SEK\n\n-  **Utrustning och Verktyg:** 300,000 SEK\n\n-  **Licenser:** 200,000 SEK\n\n-  **Marknadsföring:** 400,000 SEK\n\n-  **Övriga kostnader:** 100,000 SEK\n\n-  **Total budget:** 2 miljoner SEK\n\nKvalitetskrav:\n\n-  **Prestanda:** Applikationen ska ladda inom 2 sekunder och svarstiden\n   för användarinteraktioner ska vara under 1 sekund.'}, {'filepath': './documents2/Budget_-_Helhälsa.docx', 'text': '**Budget för HelHälsa Mobilapplikation:**\n\nIntroduktion:\n\nBudgetdokumentet syftar till att tillhandahålla en detaljerad ekonomisk\nplan för utveckling och lansering av HelHälsa mobilapplikation. Detta\ndokument omfattar alla kostnadskategorier som är associerade med\nprojektet, inklusive personal, utrustning och verktyg, licenser,\nmarknadsföring och övriga kostnader.'}, {'filepath': './documents2/state_of_the_union_2023.txt', 'text': 'That’s a lot of savings for the federal government. And, by the way, why wouldn’t we want that? Now, some members here are threatening — and I know it’s not an official party position, so I’m not going to exaggerate — but threatening to repeal the Inflation Reduction Act. As my coach — that’s okay. That’s fair. As my football coach used to say, “Lots of luck in your senior year.”\n\nMake no mistake, if you try anything to raise the cost of prescription drugs, I will veto it.'}]",
        "usr_prompt": "Vad var budjeten för projektet?"
    },
    {
        "sys_prompt": """
            ---
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
    Licenser: 200,000 SEKMarknadsföring: 400,000 SEKÖvriga kostnader: 100,000 SEKTotal budget: 2 miljoner SEKKvalitetskrav:Prestanda: Applikationen ska ladda inom 2 sekunder och svarstiden för användarinteraktioner ska vara under 1 sekund.Säkerhet: Applikationen ska uppfylla alla relevanta säkerhetsstandarder inklusive GDPR.Användarvänlighet: Applikationen ska vara intuitiv och enkel att använda, med en hög nivå av användartillfredsställelse.Riskhantering:Tekniska Risker: Såsom buggar, fel i tredjepartsintegrationer och hårdvaruproblem.Säkerhetsrisker: Såsom dataintrång och förlust av användardata.Juridiska Risker: Såsom överensstämmelse med dataskyddslagar och andra relevanta regelverk.Planering: Identifiering, bedömning, och hantering av risker genom regelbunden översyn och förberedande åtgärder.Kommunikationsplan:
        """,
        "usr_prompt": """
    När börjar utvecklingsfasen för projektet? svara på svenska!
    """
    }
]

standard_prompts = [
    'Vad är den totala budgeten för HelHälsa projektet?',
    'Kan du sammanfatta ekonomin för HelHälsa mobilapplikation i en tabell?',
    'Kan du sammanställa projektets kvalitetskrav i en tabell?',
    'Hur lång tid kommer projektet HelHälsa att ta?',
    'Sammanfatta projektplanen för HelHälsa Mobilapplikation.',
    'Vad behöver jag veta som utvecklare för HelHälsa Mobilapplikation?',
    'Var ligger Strömsholm?',
    'How do you cook chicken tikka masala'
]
