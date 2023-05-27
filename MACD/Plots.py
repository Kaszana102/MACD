import matplotlib.pyplot as plt
import numpy as np

def PlotAll(dates, price, macd, signal, money, shares):
    # plot1 - wykres cen od daty
    # plot2 - wykres macd i signal od daty
    # plot3 - wykres zarobkow jakąś strategią
    # plot4 - wykres ilości akcji od daty
    plot1 = plt.subplot2grid((12, 3), (0, 0), rowspan=2, colspan=3)
    plot2 = plt.subplot2grid((12, 3), (4, 0), rowspan=2, colspan=3)
    plot3 = plt.subplot2grid((12, 3), (8, 0), rowspan=2, colspan=3)
    plot4 = plt.subplot2grid((12, 3), (11, 0), rowspan=1, colspan=3)

    # plot1
    plot1.plot(dates, price, label="price")

    plot1.set_xlabel("date")
    plot1.set_ylabel("price [$]")
    plot1.set_title("Action prices")
    plot1.set_yticks(np.arange(0, 61, 20))

    # plot2
    plot2.plot(dates, macd, label="macd")
    plot2.plot(dates, signal, label="signal")

    plot2.set_xlabel("date")
    plot2.set_ylabel("value")
    plot2.set_title("MACD & SIGNAL")
    # plot3
    # tu będzie zarobki czy coś wykes
    plot3.plot(dates, money, label="income")

    plot3.set_xlabel("date")
    plot3.set_ylabel("money [$]")
    plot3.set_title("Actual Money in the wallet")
    plot3.set_yticks(np.arange(0, 25001, 5000))

    # plot4
    # tu będzie zarobki czy coś wykes
    plot4.bar(dates, shares, label="shares")

    plot4.set_xlabel("date")
    plot4.set_ylabel("amount")
    plot4.set_title("shares number")
    plot4.set_yticks(np.arange(0, 1101, 500))

    # wyswietlenie na osi x tylko co 20 daty
    OMIT_DATES = 20  # co którą datę wyświetlić na osi
    plot1.set_xticks(dates[::OMIT_DATES])
    plot1.set_xticklabels(dates[::OMIT_DATES], rotation=90, fontdict={'fontsize': 7})
    plot2.set_xticks(dates[::OMIT_DATES])
    plot2.set_xticklabels(dates[::OMIT_DATES], rotation=90, fontdict={'fontsize': 7})
    plot3.tick_params(labelbottom=False, bottom=False, top=False)
    plot3.set_xticks(dates[::OMIT_DATES])
    # plot3.set_xticklabels(dates[::OMIT_DATES], rotation=90, fontdict={'fontsize':7})
    plot4.set_xticks(dates[::OMIT_DATES])
    plot4.set_xticklabels(dates[::OMIT_DATES], rotation=90, fontdict={'fontsize': 7})

    # legenda
    plot2.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1, fontsize=6)

    # ustawienie rozmiaru okna
    fig = plt.gcf()
    fig.set_size_inches(16, 8)

    plot1.grid()
    plot2.grid()
    plot3.grid()
    plot4.grid()
    plt.show()


def Plot2(dates, price, macd, signal):
    # plot1 - wykres cen od daty
    # plot2 - wykres macd i signal od daty
    # plot3 - wykres zarobkow jakąś strategią
    # plot4 - wykres ilości akcji od daty
    plot1 = plt.subplot2grid((5, 2), (0, 0), rowspan=2, colspan=2)
    plot2 = plt.subplot2grid((5, 2), (3, 0), rowspan=2, colspan=2)

    # plot1
    plot1.plot(dates, price, label="price")

    plot1.set_xlabel("date")
    plot1.set_ylabel("price [$]")
    plot1.set_title("Action prices")
    plot1.set_yticks(np.arange(0, 61, 10))

    # plot2
    plot2.plot(dates, macd, label="macd")
    plot2.plot(dates, signal, label="signal")

    plot2.set_xlabel("date")
    plot2.set_ylabel("value")
    plot2.set_title("MACD & SIGNAL")
    plot2.set_yticks(np.arange(-5, 5.1, 1))
    # wyswietlenie na osi x tylko co 20 daty
    OMIT_DATES = 20  # co którą datę wyświetlić na osi
    plot1.set_xticks(dates[::OMIT_DATES])
    plot1.set_xticklabels(dates[::OMIT_DATES], rotation=90, fontdict={'fontsize': 7})
    plot2.set_xticks(dates[::OMIT_DATES])
    plot2.set_xticklabels(dates[::OMIT_DATES], rotation=90, fontdict={'fontsize': 7})

    # legenda
    plot2.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1, fontsize=6)

    # ustawienie rozmiaru okna
    fig = plt.gcf()
    fig.set_size_inches(16, 8)

    plot1.grid()
    plot2.grid()
    plt.show()
