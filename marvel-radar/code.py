from pyecharts import options as opts
from pyecharts.charts import Radar
from pyecharts.commons.utils import JsCode

captain_america = [{"value": [4, 4, 4, 4, 1, 7], "name": "�����ӳ�"}] #ÿ������Ӣ�۵�ս������ֵ
iron_man= [{"value": [6, 3, 5, 3, 5, 3], "name": "������"}]
black_widow = [{"value": [3, 3, 2, 3, 2, 7], "name": "�ڹѸ�"}]
hawkeye = [{"value": [3, 3, 3, 2, 3, 7], "name": "ӥ��"}]
hulk = [{"value": [2, 7, 3, 7, 1, 3], "name": "�̾���"}]
thor =  [{"value": [2, 7, 6, 7, 7, 6], "name": "����"}]

myschema = [
    {"name": '����', "max": 7, "min": 0},
    {"name": '����', "max": 7, "min": 0},
    {"name": '�ٶ�', "max": 7, "min": 0},
    {"name": '����', "max": 7, "min": 0},
    {"name": '��������', "max": 7, "min": 0},
    {"name": 'ս������', "max": 7, "min": 0}
] #�����״�ͼ������
r = Radar(init_opts=opts.InitOpts(
            bg_color={"type": "pattern", "image": JsCode("img"), "repeat": "no-repeat"}
        )
) #��ʼ���״�ͼ
r.add_js_funcs(
    """
    var img = new Image(); img.src = 'a5.png';
    """
) #ִ��js����

(
    r.add_schema(
        schema=myschema,
        shape="circle", #ͼƬ��״
        center=["50%", "50%"], #ͼƬ����λ��
        radius="80%", #ͼƬ�뾶��С
        angleaxis_opts=opts.AngleAxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axislabel_opts=opts.LabelOpts(is_show=False),
            splitline_opts=opts.SplitLineOpts(is_show=False),
        ),
        radiusaxis_opts=opts.RadiusAxisOpts(
            min_=0,
            max_=7,
            interval=1,
            splitarea_opts=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
            splitline_opts=opts.series_options.SplitLineOpts(is_show=True, linestyle_opts={'color':'grey','opacity':0.8})   
            
        ),
        polar_opts=opts.PolarOpts(),
        splitline_opt=opts.SplitLineOpts(is_show=False),
        textstyle_opts=opts.TextStyleOpts(color="black"),
    )
    .add(
        series_name="�����ӳ�",
        data=captain_america,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
        linestyle_opts=opts.LineStyleOpts(width=1),
    )
    .add(
        series_name="������",
        data=iron_man,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
        linestyle_opts=opts.LineStyleOpts(width=1),
    )
    .add(
        series_name="�ڹѸ�",
        data=black_widow,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
        linestyle_opts=opts.LineStyleOpts(width=1),
    )
    .add(
        series_name="ӥ��",
        data=hawkeye,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
        linestyle_opts=opts.LineStyleOpts(width=1),
    )
    .add(
        series_name="�̾���",
        data=hulk,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
        linestyle_opts=opts.LineStyleOpts(width=1),
    )
    .add(
        series_name="����",
        data=thor,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
        linestyle_opts=opts.LineStyleOpts(width=1),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="��������ͷʵ���Ա�"), legend_opts=opts.LegendOpts()
    )
    .render('ht1.html') #������ҳ
)
