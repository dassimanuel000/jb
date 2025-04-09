
from ODDS.scripts.function import Client, analys_per_link, append_new_line, callAi, clean_text, click_consent, convert_sheet_csv, extract_list_from_google, forebet, get_domain, initGoogle, load_file, save_to_excel, scrap_selenium_v1, to_percentage



def runner():
    matches = []
    driver = scrap_selenium_v1("google.com")
    list_alerts = load_file("/media/ds/DATA/Documents/Advanced-Python/job-finder/list_alerts.txt")
    for research in list_alerts:
        initGoogle(driver)
        result_search = extract_list_from_google(driver, research, "0")
        for page in result_search:
            mots_interdits = ["india", "exclu", "exclu", "tb2l", "u21", "emplois.html?vjk=", "u19", "bulgar", "ligue-b", "-a2-", "-a2/", "2-bundesliga"]
            if page and all(mot not in page for mot in mots_interdits):
                class_web = Client(url=page, domain=get_domain(page), driver=driver, e=None)
                web_content = class_web.run()
                if web_content.title and all(mot not in web_content.title for mot in mots_interdits):
                    web_content.prompt = f"""
                        ### Prompt GPT à utiliser :
                        Tu es un assistant de parsing d'offres d'emploi. Je vais te donner un **titre** et un **contenu** d'offre d'emploi.  
                        Analyse toutes les informations disponibles et retourne un **objet JSON** structuré avec les clés suivantes :

                        ```json
                        {{
                        "keyword": "",
                        "company": "",
                        "location": "",
                        "city": "",
                        "remote": "",
                        "experience": "",
                        "salary_range": "",
                        "date_posted": "",
                        "deadline": "",
                        "link": "",
                        "status": "to_apply",
                        "priority": "normal",
                        "language": [],
                        "tech_stack": [],
                        "notes": ""
                        }}
                        ```

                        - `remote` doit être `true` ou `false` (ou `""` si inconnu).
                        - `language` et `tech_stack` doivent être des **listes** (ou vides).
                        - Si une information est absente, laisse simplement la valeur vide `""`.
                        - Le champ `status` est toujours `"to_apply"` par défaut.
                        - Le champ `priority` est `"normal"` sauf si tu détectes de l'urgence ou un fort intérêt.
                        - `notes` peut contenir toute info utile (ex: "CDI", "full remote", "culture d'entreprise", etc.).

                        Voici les données à analyser :

                        **Titre**: `{web_content.title}`

                        **Contenu**:
                        ```
                        {clean_text(web_content.xml_result)}
                        ```

                        """
                    print('Z')
                    json_result = callAi(web_content.prompt)
                    if json_result:
                        if len(json_result) > 0:
                            match_info = {
                                "title": web_content.title,
                                "keyword": json_result["keyword"],
                                "company": json_result["company"],
                                "location": json_result["location"],
                                "city": json_result["city"],
                                "remote": json_result["remote"],
                                "experience": json_result["experience"],
                                "salary_range": json_result["salary_range"],
                                "date_posted": json_result["date_posted"],
                                "deadline": json_result["deadline"],
                                "link": page,
                                "status": json_result["status"],
                                "priority": json_result["priority"],
                                "language": json_result["language"],
                                "tech_stack": json_result["tech_stack"],
                                "notes": json_result["notes"],
                            }
                            append_new_line('analyse-log.txt', str(match_info))
                            matches.append(match_info)
    save_to_excel(matches, "JOB-LISTING.xlsx")
runner()