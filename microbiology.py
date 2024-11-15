def micro(time, pos_list):
    for i in pos_list:
        if str(i[0]).lower() == "fever" or str(i[0]).lower() == "temperature":
            if (str(list(time)[-1]).lower() == "m" or str(list(time)[-1]).lower() == "y" or str(
                    list(time)[-1]).lower() == "w") or (int(list(time)[0]) > 7 and str(list(time)[-1]).lower() == "d"):
                # Chronic disease
                for _ in pos_list:
                    # HIV
                    if _[0].lower() == "swelling":
                        for a in pos_list:
                            if a[0].lower() == "shoulder" or a[0].lower() == "hips" or a[0].lower() == "butt" or a[
                                0].lower() == "buttocks" or a[0].lower() == "neck" or a[0].lower() == "chest":
                                return "result/The diagnosis is HIV."
                    # Tuberculosis
                    elif _[0].lower() == "night":
                        for z in pos_list:
                            if z[0].lower() == "sweating" or z[0].lower() == "sweats" or z[0].lower() == "sweat":
                                return "result/The diagnosis is Tuberculosis."
                    # Malnutrition
                    elif _[0].lower() == "growth":
                        for y in pos_list:
                            if y[0].lower() == "stunted" or y[0].lower() == "low" or y[0].lower() == "less":
                                return "result/The diagnosis is Malnutrition."
                    # Chronic infection
                    elif _[0].lower() == "weight":
                        for x in pos_list:
                            if x[0].lower() == "low" or x[0].lower() == "less" or x[0].lower() == "decreasing":
                                return "result/The diagnosis is Chronic Infection."

            elif int(list(time)[0]) <= 7 and str(list(time)[-1]).lower() == "d":
                # Acute disease
                for b in pos_list:
                    # Malaria
                    if b[0].lower() == "cold" or b[0].lower() == "cool" or b[0].lower() == "chills" or b[0].lower() == "chill":return "result/The diagnosis is Malaria."
                    # Typhoid
                    elif b[0].lower() == "hunger" or b[0].lower() == "stomach" or b[0].lower() == "eating" or b[0].lower() == "eat" or b[0].lower() == "food":
                        for c in pos_list:
                            if c[0].lower() == "no" or c[0].lower() == "less" or c[0].lower() == "full" or c[0].lower() == "feel":
                                return "result/The result is Typhoid."
                    # Dengue
                    elif b[0].lower() == "nose":
                        for d in pos_list:
                            if d[0].lower() == "bleeding" or d[0].lower() == "bleed" or d[0].lower() == "bleeds" or d[
                                0].lower() == "blood":
                                return "result/The diagnosis is Dengue."
                    # Viral infection
                    elif b[0].lower() == "cough" or b[0].lower() == "nose":
                        for e in pos_list:
                            if e[0].lower() == "running" or e[0].lower() == "runny" or e[0].lower() == "mucus":
                                return "result/The diagnosis is Viral Infection."
