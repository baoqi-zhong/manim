from manimlib.imports import *

# 左右：-7 7
# 上下 4-4
# f=2
class test(Scene):
    def construct(self):
        self.first()
        self.main_()

    def first(self):

        text1 = Text('“上帝说，要有光，~~~~~\n\n于是课本就有了凸透镜成像”', font='思源字体 blod', size=0.5, stroke_width=1).to_edge(UP).shift(LEFT * 3)
        text1[23:-1].set_color(ORANGE)
        text1[9:14].set_color(BLACK)
        who = Text('——沃·资基硕德', font='思源字体 blod', size=0.5, stroke_width=1).next_to(text1, DR).set_color(YELLOW).shift(LEFT)

        text1_eng = Text('“God said, there should be light, ~~~~~\nso the textbook has convex lens imaging”', font='思源字体 blod', size=0.5, stroke_width=1).shift(DOWN+LEFT)
        text1_eng[59:-1].set_color(ORANGE)
        text1_eng[34:40].set_color(BLACK)
        who_eng = Text('——By·myself', font='思源字体 blod', size=0.5, stroke_width=1).next_to(text1_eng, DR).set_color(YELLOW).shift(LEFT*2)

        self.stayable = Text('凸透镜成像可视化', font='思源字体 blod', size=0.3, stroke_width=1).to_edge(UR).shift(DOWN)

        self.play(LaggedStart(*[
                    FadeIn(i) for i in text1
                ], Write(text1_eng),run_time=8))
        time.sleep(2)
        self.play(Write(who), Write(who_eng), run_time=3)

        self.wait(3)
        self.play(ReplacementTransform(Group(text1, text1_eng, who_eng, who), self.stayable))

        self.wait(1)

    def main_(self):
        line_mian_light = Line(np.array([-7, 0, 0]), np.array([7, 0, 0]))
        glass = Ellipse(width=.6, height=3)
        f = Dot(np.array([-2, 0, 0]))
        f2 = Dot(np.array([-4, 0, 0]))
        f_ = Dot(np.array([2, 0, 0]))
        f2_ = Dot(np.array([4, 0, 0]))
        f_word = TextMobject('f', color=BLUE)
        f_word.next_to(f, UP)
        f2_word = TextMobject('2f', color=BLUE)
        f2_word.next_to(f2, UP)
        f__word = TextMobject('f', color=BLUE)
        f__word.next_to(f_, UP)
        f2__word = TextMobject('2f', color=BLUE)
        f2__word.next_to(f2_, UP)

        arrow_wu = TextMobject('↑')
        arrow_wu.scale(3)
        arrow_wu.shift(np.array([-1, 0.7, 0]))

        light1 = Line()
        light1.add_updater(lambda l: l.put_start_and_end_on(arrow_wu.get_center() + UP * 0.7, np.array([0, 1.4, 0])))
        light1_2 = Line()
        light1_2.add_updater(lambda l: l.put_start_and_end_on(np.array([0, 1.4, 0]), np.array([2, -1.4, 0])*6+np.array([0, 1.4, 0])))
        light2 = Line()
        light2.add_updater(lambda l:l.put_start_and_end_on(arrow_wu.get_center()+UP*0.7, -(arrow_wu.get_center()+UP*0.7)*10 ))


        def get_jiao(l):
            if arrow_wu.get_center()[0] != -2:
                l.move_to([1.4 / ( 0.7 + 1.4 / arrow_wu.get_center()[0] ),
                 1.4 - 1.4 / ( 0.7 + 1.4 / arrow_wu.get_center()[0] ) * 0.7, 0])

        jiao = Dot(color=RED)
        jiao.add_updater(get_jiao)

        word_1 = TextMobject('u$>$2f  f$<$v$<$2f')
        word_1.shift(np.array([-5,3,0]))
        w1_c = Text('倒立缩小实像-照相机', font='思源字体 blod', size=0.5, stroke_width=1).next_to(word_1, RIGHT)
        w1_c[7:].set_color(YELLOW)

        word_2 = TextMobject('u=2f  v=2f')
        word_2.shift(np.array([-5, 3, 0]))
        w2_c = Text('倒立等大实像', font='思源字体 blod', size=0.5, stroke_width=1).next_to(word_2, RIGHT)

        word_3 = TextMobject('f$<$u$<$2f  v$>$2f')
        word_3.shift(np.array([-5, 3, 0]))
        w3_c = Text('倒立放大实像-投影仪', font='思源字体 blod', size=0.5, stroke_width=1).next_to(word_3, RIGHT)
        w3_c[7:].set_color(YELLOW)

        word_4 = TextMobject('u$=$f  no image')
        word_4.shift(np.array([-5, 3, 0]))
        w4_c = Text('不成像', font='思源字体 blod', size=0.5, stroke_width=1).next_to(word_4, RIGHT)

        word_5 = TextMobject('u$<$f')
        word_5.shift(np.array([-5, -3, 0]))
        w5_c = Text('正立放大虚像-放大镜', font='思源字体 blod', size=0.5, stroke_width=1).next_to(word_5, RIGHT)
        w5_c[7:].set_color(YELLOW)

        wu = Text('物体', font='思源字体 blod', size=0.4, stroke_width=1)
        wu.add_updater(lambda d: d.next_to(arrow_wu, UP))

        def get_xiang(x):
            if arrow_wu.get_center()[0] != -2:
                x.put_start_and_end_on(np.array([1.4 / (0.7 + 1.4 / (arrow_wu.get_center()[0])),
                                            1.4 - 1.4 / (0.7 + 1.4 / (arrow_wu.get_center()[0])) * 0.7, 0]),
                                  np.array([1.4 / (0.7 + 1.4 / (arrow_wu.get_center()[0])), 0, 0]))
        xiang = Line(color=BLUE, stroke_width=10)
        xiang.add_updater(get_xiang)

        image = Text('像', font='思源字体 blod', size=0.5, stroke_width=1)
        image.add_updater(lambda d: d.next_to(xiang, UP))

        def get_fan_1(f):
            f.put_start_and_end_on(jiao.get_center(), [0, 1.4, 0])
        def get_fan_2(f):
            f.put_start_and_end_on(jiao.get_center(), arrow_wu.get_center() + UP * 0.7)

        fan_1 = Line(color=GRAY)
        fan_1.add_updater(get_fan_1)
        fan_2 = Line(color=GRAY)
        fan_2.add_updater(get_fan_2)

        self.play(ShowCreation(line_mian_light),ShowCreation(glass))
        self.wait(1)
        self.play(FadeInFromLarge(f), FadeInFromLarge(f2), FadeInFromLarge(f_), FadeInFromLarge(f2_))
        self.play(FadeInFromLarge(f_word), FadeInFromLarge(f2_word), FadeInFromLarge(f__word), FadeInFromLarge(f2__word))

        self.wait(1.5)
        self.play(FadeIn(arrow_wu), Write(wu), run_time=1)
        self.wait(1)

        self.play(ApplyMethod(arrow_wu.shift, LEFT*5.5))
        self.wait(2)
        self.play(ShowCreation(light1))
        self.play(ShowCreation(light1_2))
        self.play(ShowCreation(light2))

        self.wait(2)
        self.play(FadeInFromLarge(jiao))
        self.wait(0.8)
        self.play(ShowCreation(xiang), Write(image), run_time=1)
        self.wait(1)

        self.play(Write(word_1), Write(w1_c))
        self.wait(5)
        self.play(ApplyMethod(arrow_wu.shift, RIGHT*2.5))
        self.play(ReplacementTransform(word_1, word_2), ReplacementTransform(w1_c, w2_c))
        self.wait(5)
        self.play(ApplyMethod(arrow_wu.shift, RIGHT))
        self.play(ReplacementTransform(word_2, word_3), ReplacementTransform(w2_c, w3_c))
        self.wait(5)
        self.play(ApplyMethod(arrow_wu.shift, RIGHT))
        self.play(ReplacementTransform(word_3, word_4), ReplacementTransform(w3_c, w4_c))
        self.wait(5)
        self.add(fan_1)
        self.add(fan_2)

        self.play(ApplyMethod(arrow_wu.shift, RIGHT))
        self.play(ReplacementTransform(word_4, word_5), ReplacementTransform(w4_c, w5_c))

        self.wait(5)
        self.play(FadeOut(self.stayable), FadeOut(line_mian_light), FadeOut(glass), FadeOut(f), FadeOut(f2), FadeOut(f_), FadeOut(f2_), FadeOut(f_word), FadeOut(f2_word), FadeOut(f__word), FadeOut(f2__word), FadeOut(light1), FadeOut(light1_2), FadeOut(light2), FadeOut(xiang), FadeOut(arrow_wu), FadeOut(jiao), FadeOut(w5_c), FadeOut(word_5), FadeOut(fan_1), FadeOut(fan_2), FadeOut(image), FadeOut(wu), run_time=2.3)
        self.wait(2)
        coin = SVGMobject('./my_svg/coin.svg')
        good = SVGMobject('./my_svg/good.svg')
        good.shift(LEFT * 3)
        favo = SVGMobject('./my_svg/favo.svg')
        favo.shift(RIGHT * 3)
        group = Group(coin, good, favo)

        mk = Text('MKnb', font='思源字体 blod', stroke_width=1)
        mk[0].set_color(BLUE)
        mk[1].set_color(LIGHT_BROWN)
        mk.scale(0.8)

        self.play(Write(coin), Write(good), Write(favo), run_time=3)
        self.wait(1)
        self.play(ReplacementTransform(group, mk))
        self.wait(2)
        self.play(FadeOutAndShiftDown(mk))
        self.wait(1)



if __name__ == '__main__':
    os.system('python manim.py -p --high_quality wuli.py test')# -l -p
