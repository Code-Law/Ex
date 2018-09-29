import matplotlib.pyplot as plt

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2., 1.03 * height, '%s' % float(height))

plt.xlabel(u'sex')
plt.ylabel(u'count')

plt.title(u"Sex Ratio Analyse")
plt.xticks((0, 1), (u'M', u'F'))
rect = plt.bar(left=(0, 1), height=(1, 0.5), width=0.35, align="center")

plt.legend((rect,), (u"Chart",))
autolabel(rect)

plt.show()