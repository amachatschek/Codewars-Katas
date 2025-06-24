def is_orthogonal(u, v):                    # Der Funktion werden 2 gleich-lange Listen mit ganzen Zahlen übergeben. Die Erste ist "u", die Zweite ist "v".
    vsum = 0                                # Variable vsum, die später die Summe von {a1*b1 + a2*b2 + a3*b3 + ... + aN*bN} speichert, wird definiert.
    for i in range(len(u)):                 # FÜR i (repräsentiert jeden Durchlauf) IN der Reichweite der Anzahl an Einträgen im Array/Liste "u", führe folgenden Block aus: 
        v_multiply = u[i] * v[i]            # Speichere u[Eintrag 1, dann 2, dann 3...] * v[Eintrag 1, dann 2, dann 3...] in "v_multiply"...
        vsum += v_multiply                  # ...und addiere dann die Summe des jeweiligen Durchlaufs zu dem Wert in "vsum". Wird nacheinander für jeden Wert in u ausgeführt.
    return True if vsum == 0 else False     # Gib True wieder, falls vsum = 0 ist, sonst gib False wieder.


print(is_orthogonal([1,-2,3,-4], [-4,3,2,-1]))  # Funktion wird aufgerufen mit u = [1,-2,3,-4] und v = [-4,3,2,-1]
                                                # 
                                                # "True" wird in der Konsole angezeigt, wenn das Skalarprodukt beider Vektoren 0 ist.