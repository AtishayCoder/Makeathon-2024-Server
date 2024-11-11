def micro(time, pos_list):
    for i in pos_list:
        if str(i[0]).lower() == "fever":
            if str(list(time)[-1]).lower() == "m" or str(list(time)[-1]).lower() == "y" or str(list(time)[-1]).lower() == "w":
                # Chronic disease
                pass
            elif int(list(time)[0]) > 7 and str(list(time)[-1]).lower() == "d":
                # Chronic disease
                pass
            elif int(list(time)[0]) <= 7 and str(list(time)[-1]).lower() == "d":
                # Acute disease
                pass
            else:
                pass
