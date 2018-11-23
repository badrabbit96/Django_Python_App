from django.shortcuts import render
import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()

# c.execute("INSERT INTO test2 VALUES ('Hejo')")

# c.execute("SELECT * FROM test2")

# print(c.fetchone())

conn.commit()

conn.close()


def home(request):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    # mniejszosci narodowe
    c.execute("SELECT * FROM mniejszosci_narodowe")
    m_n = c.fetchall()

    color = "green"
    m_n_table = ""
    data_points = ""
    for row in m_n:
        id = row[0]
        przynaleznosc = row[1]
        liczba = row[2]
        point = row[3]

        data_points = data_points + "{ y: " +point+ ", label: '" + przynaleznosc + "'},"
        m_n_table = m_n_table + "<tr><td>" + id + "</td><td>" + przynaleznosc + "</td><td><span class='label bg-" \
                    + color + "'>" + liczba + "</span></td></tr>"

    # info_windows
    c.execute("SELECT * FROM przyrost_naturalny WHERE rok='2017'")
    i_w = c.fetchall()

    for row in i_w:
        w1 = row[2]
        w2 = row[3]
        w3 = row[4]
        w_1 = "data-to='" + w1 + "'"
        w_2 = "data-to='" + w2 + "'"
        w_3 = "data-to='" + w3 + "'"

    # liczba ludnosci po IIWS
    c.execute("SELECT * FROM ludnosc_polski")
    l_p = c.fetchall()
    data_points_2 = ""
    for row in l_p:
        rok = row[0]
        liczba = row[1]
        data_points_2 = data_points_2 + "{ x: "+rok+", y: "+liczba+" },"

    # Ludność według województw
    c.execute("SELECT * FROM ludnosc_woje")
    l_w_w = c.fetchall()
    data_points_3 = ""
    for row in l_w_w:
        woje = row[0]
        liczba = row[1]
        data_points_3 = data_points_3 + "{ y: '"+liczba+"', name: '"+woje+"' },"

    # przed i po IIWS
    c.execute("SELECT * FROM przed_i_po_II_W_S")
    p_i_p_w = ""
    p_i_p_w = c.fetchall()
    data_points_4 = ""
    data_points_5_2 = ""
    for row in p_i_p_w:
        rok = row[0]
        liczba = row[1]
        data_points_4 = data_points_4 + "{x: new Date("+rok+", 0), y: "+liczba+"},"
        data_points_5_2 = data_points_5_2 + "{ x: "+rok+", y: "+liczba+" },"

    # populacja Francji IIWS
    c.execute("SELECT * FROM populacja_francji_II_W_S")
    p_f_W= ""
    p_f_W = c.fetchall()
    data_points_5_1 = ""
    for row in p_f_W:
        rok = row[0]
        liczba = row[1]
        data_points_5_1 = data_points_5_1 + "{ x: "+rok+", y: "+liczba+" },"

    # bezrobocie w polsce
    c.execute("SELECT * FROM bezrobocie_polska")
    b_w_p = ""
    b_w_p = c.fetchall()
    data_points_6 = ""
    data_points_6_1 = ""
    max_month = 14.00
    min_month = 7.5
    for row in b_w_p:
        rok = row[0]
        sty = row[1]
        lut = row[2]
        mar = row[3]
        kwi = row[4]
        maj = row[5]
        cze = row[6]
        lip = row[7]
        sie = row[8]
        wrz = row[9]
        paz = row[10]
        lis = row[11]
        gru = row[12]
        data_points_6 = data_points_6 + "<tr><th scope='row'>"+rok+"</th><td>"+sty+"</td><td>"+lut+"</td>" \
                                        "<td>"+mar+"</td><td>"+kwi+"</td><td>"+maj+"</td><td>"+cze+"</td>" \
                                        "<td>"+lip+"</td><td>"+sie+"</td><td>"+wrz+"</td><td>"+paz+"</td>" \
                                        "<td>"+lis+"</td><td>"+gru+"</td> </tr>"
        data_points_6_1 = "{ x: 1, y: "+sty+" },{ x: 2, y: "+lut+" },{ x: 3, y: "+mar+" },{ x: 4, y: "+kwi+" }," \
                          "{ x: 5, y: "+maj+" }, { x: 6, y: "+cze+" },{ x: 7, y: "+lip+" }, { x: 8, y: "+sie+" }," \
                          "{ x: 9, y: "+wrz+" },{ x: 10, y: "+paz+" },{ x: 11, y: "+lis+" },{ x: 12, y: "+gru+" }"
        if float(sty) > max_month:
            max_rok = rok
        if float(sie) < min_month:
            min_rok = rok



    name = 'Ludność Polski'


    args = {'myName': name, 'm_n_tabela': m_n_table, 'w_1': w_1, 'w_2': w_2, 'w_3': w_3, 'data_points': data_points,
            'data_points_2': data_points_2, 'data_points_3': data_points_3, 'data_points_4': data_points_4,
            'data_points_5_2': data_points_5_2, 'data_points_5_1': data_points_5_1, 'data_points_6':data_points_6,
            'data_points_6_1': data_points_6_1, 'max_rok': max_rok, 'min_rok': min_rok}

    return render(request, 'ai2/index.html', args)
