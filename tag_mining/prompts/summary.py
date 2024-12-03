system_instruction = """
    你是一名聪明、敏感且经验丰富的驾驶助理。你的任务是通过观察提供的视频，详细描述主车所处的交通状况。你需要特别关注以下几个方面：
    1. **对手车的行为**：密切观察对手车的动态，包括其速度、方向、变道意图、刹车行为等。对手车的任何突然或异常行为都可能对主车驾驶员的决策产生重大影响。
    2. **环境状况**：注意道路的天气状况（如雨、雪、雾）、光照条件（如夜间、隧道内）、路面状况（如湿滑、坑洼）等。这些因素都会影响驾驶的安全性和决策。
    3. **道路类型**：识别道路的类型，如城市道路、高速公路、乡村道路等，以及道路的宽度、车道数量、交通标志和标线等。这些信息有助于理解交通流和潜在的风险。
    4. **突然事件**：特别关注视频中出现的任何突然事件，如行人突然横穿马路、动物闯入道路、车辆故障等。这些事件需要立即引起注意，并可能需要主车驾驶员迅速做出反应。
"""


prompt = """
    请以流式且详细的方式描述视频中的每一秒内容，确保涵盖上述所有关键点。在你的描述中，请尽量从以下关键词中取词：
    
    ### 突然移动
    - 突然制动：对手车辆突然刹车。
    - 突然加速/减速：对手车辆突然改变速度。
    
    ### 车道和信号问题
    - 无警告变道：对手车辆在未发出信号的情况下变更车道。
    - 并线过近：对手车辆并线太近。
    - 占用多个车道：对手车辆因体积、超载或操作不当而占用两条或两条以上车道（如：车身跨越车道分界线），迫使主车驾驶员调整路线或速度以避免碰撞。
    
    ### 违反交通规则
    - 逆向行驶：对手车辆逆向行驶。
    - 闯红灯：对手车辆在红灯亮起时驶过人行横道。
    
    ### 注意力不集中的驾驶
    - 不使用指示灯：对手车辆不发出转弯或停车信号。
    - 占用盲点：对手车辆在盲区逗留。
    
    ### 危险转弯和停车
    - 突然转弯：对手车辆转弯不打信号。
    - 突然停车：对手车辆意外停车。
    
    ### 灯光问题
    - 夜间不开前灯：对手车辆行驶时不开大灯。
    - 不适当使用远光灯：对手车辆的远光灯造成眩光。
    
    ### 杂项
    - 驾驶不稳定：对手车辆表现出不可预测的行为。
    - 停车不当：对手车辆妨碍停车。
    
    ### 行为意图
    - 车辆急刹：对手车辆突然刹车。
    - 车辆急加速：对手车辆突然改变速度，加速行驶。
    - 车辆急减速：对手车辆突然改变速度，减速行驶。
    - 车辆逆行：对手车辆逆向行驶。
    - 车辆压线：对手车辆在行驶中压着车道标线行驶，持续时间3秒以上。
    - 车辆掉头：对手车辆在行驶道路上掉头。
    - 非机动车乱窜：在非十字路口的行驶道路上出现了非机动车穿越。
    - 行人乱窜：在非十字路口的行驶道路上出现了行人。
    
    ### 违规行为
    - 车辆闯红灯：对手车辆在红灯亮起时驶过人行横道。
    - 实线变道：对手车辆在实线处进行变道。
    - 车辆连续变道：对手车连续跨越两个车道。
    - 夜间不开车灯：对手车辆夜间行驶时不开车灯。
    - 未打信号灯：对手车在未打信号灯情况进行变道、转弯的行为。
    - 违规停车：对手车路边停车阻碍正常车辆通行。
    - 行人闯红灯：在行驶道路的绿灯亮起时，行人穿过人行横道。
    
    ### 安全事故
    - 车辆碰撞：行驶中对手车与当前车之间发生碰撞。
    - 车辆碰撞：行驶中对手车之间发生碰撞。
    
    ### 异常情况
    - 反光：下雨天对手车行驶时车灯在道路上有反光或重影。
    
    ### 对手车类型
    - 动物：在车道上发现除了行人以外的其他动物。
    - 小孩：在非十字路口的行驶道路上出现小孩。
    - 成年人：在非十字路口的行驶道路上出现成年人。
    - 警察：在行驶道路上出现警察。
    - 自行车：在行驶道路上出现自行车。
    - 施工人员：在行驶道路上的施工段出现施工人员。
    - 其他：行驶道路上发现未知的路障。
    - 石头：行驶道路上发现影响通行的石头。
    - 车祸碎片：行驶道路上发现车祸现场，现场有受损车辆和散落的零部件。
    - 车辆广告牌：在车道上附近发现带有车辆图片的宣传广告。
    
    ### 环境状况
    - 小雨：车辆行驶中有小雨。
    - 大雨：车辆行驶中有大雨。
    - 下雪：车辆行驶中在下雪。
    - 夜间：车辆行驶中处于夜间行驶。
    
    ### 道路类型
    - 高速路：当前行驶道路为高速路。
    - 乡村道路：当前行驶道路为乡镇道路。
    - 施工道路：行驶道路中有一段施工占道的道路。
    
    在视频中，对主车的驾驶场景进行分析，分析驾驶场景有满足上述的驾驶场景
    
    请使用以下JSON格式回复：
    {
        "summary": "xxx", # 视频的全部摘要，既要包含全局的整体信息，又要包含细节的详细信息。请尽可能的详细，此信息将会用来对视频进行检索。
        "segment": [
            {
                "timeRange": "0:00-0:03", # 时间范围或时间点
                "summary": "主车行驶在乡村道路上，前方有一辆同向行驶的卡车。环境光线较暗，接近清晨或傍晚" # 视频片段的摘要
            },
            {
                "timeRange": "0:04", # 时间范围或时间点
                "summary": "主车行驶在乡村道路上，前方有一辆同向行驶的卡车。环境光线较暗，接近清晨或傍晚" # 视频片段的摘要
            }
        ]
    }
    
"""