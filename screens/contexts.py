HELP_CONTEXT = [
    {
        'name': 'SHOOT',
        'key': 'SPACE'
    },
    {
        'name': 'MOVE LEFT',
        'key': 'LEFT'
    },
    {
        'name': 'MOVE RIGHT',
        'key': 'RIGHT'
    },
    {
        'name': 'MOVE DOWN',
        'key': 'DOWN'
    },
    {
        'name': 'MOVE UP',
        'key': 'UP'
    }
]




SETTING_CONTEXT = [
    {
        'name': 'SPEED UP',
        'key': '<'
    },
    {
        'name': 'SPEED DOWN',
        'key': '>'
    },
    {
        'name': 'MUTE AUDIO',
        'key': 'M'
    },
    {
        'name': 'VOLUME UP/DOWN',
        'key': '+/-'
    }
]

LOADING_CONTEXT = [
    {
        'text': 'PLAY',
        'action': 'game'
    },
    {
        'text': 'SCORES',
        'action': 'score'
    },
    {
        'text': 'SUMMARY',
        'action': 'summary'
    },
    {
        'text': 'SETTING',
        'action': 'setting'
    },
    {
        'text': 'Help',
        'action': 'help',
    },


]

EXPLAIN_CONTEXT = {
    'begin': [
        {
            'stage': 1,
            'text': [
                '000 대..원... ㄷ...어..라...',
                '현ㅈ... 외계 ..ㅁ..체.... 지구...를 ㅊ..략 했다....',
                '그ㄷ..이 현재 지구 생..명..ㅊ... ㅈ종... 시작 했....',
                '다...시.. 한....번 반ㅂ... 한다...',
                '현... 외계 ㅅ...명..체.... ㅈ...구... 침.. ㅎ..다..',
                '통...ㅅ..이... ㅈ...지.. 못하...다....',
                '조종 당...ㅎ..는... 지..ㄱ...생....를 ㅁ..찔...라...',
                '빠ㄹ...게.... 정...리..ㅎ...도...록...행..ㅇ.... 비..네...',
            ]
        },
        {
            'stage': 2,
            'text': [
                '000 대..원... 고....ㅅ..많았....다...',
                '지구..생..ㅁ..체를...처...ㄹ..하...느...라...',
                '하...ㅈ..만...아...직... 끝ㅇ...난..ㄱ..아..니..네..',
                '우ㄹ..는... 이..들의... 우...ㅈ...로...쫓ㅇ..낼거...네..',
                '다..ㅅ..는.. 지..구를.. 침..ㄹ..하지..못..하도..ㄹ...',
                '이들..은...전..ㄴ.. 다..게.. 공..ㄱ.. 조심...하..ㄷ..록',
                '보...ㅇ..는.. 모....ㄷ..적들... 을.. 무ㅉ...르도...록...',
                'ㅃ..르..게.. 정...ㄹ...하...ㄷ...록...ㅎ..운을... ㅂ..네...',
            ]
        },
        {
            'stage': 3,
            'text': [
                '000 대..원... 고....ㅅ..많았....다...',
                '지구..ㅈ..ㅜ변의..외계..생명..ㅊ..ㅔ..는',
                'ㅁㅗ..두..정리..ㄷ..ㅗ..ㅣ었다...',
                '하...ㅈ...ㅣ...만...언...ㅈ...ㅔ...ㄴ...가...다시....',
                '그들ㅇ...ㅣ...침랴...ㄱ...ㅎ...ㅐ...올...것이ㄷ...ㅏ....',
                '다..ㅅ..는.. 지..구를.. 침..ㄹ..하지..못..하도..ㄹ...',
                '이..ㅂ..에는..ㅇ..ㅜ리가...먼ㅈ.ㅓ..ㅅ...공ㅎ..ㅏ자...',
                '출격ㄱ...ㅕㄱ...하라...!!',
            ]
        },
    ],
    'dying': {
        'stage': 'Ending',
        'text': [
            '지구를 지키지 못했다...',
            '지구 생명체들은 모두 최면에 걸려 노예가 되었다...',
            '외계 생명체에 의해 우리의 지구는 더이상 푸른 별이 아니다...',
            '그들의 식민지일 뿐이다...'
        ]
    }
}

# SUMMARY_CONTEXT = [
#     {
#         'text': 'Life on Earth is in danger due ',
#     },
#     {
#         'text': 'to the invasion of extraterrestrial planets',
#     },
#     {
#         'text': 'It defeats the controlled life on Earth',
#     },
#     {
#         'text': 'After defeating the fleet surrounding the earth,',
#     },
#     {
#         'text': 'Let\'s go get revenge on the alien planet.'
#     }
# ]

SUMMARY_CONTEXT = [
    {
        'text': '외계행성의 침공으로 지구 생명체들이 위험하다 ',
    },
    {
        'text': '조종당하는 지구생명체를 무찌르고',
    },
    {
        'text': '지구를 둘러싼 함대를 격파한 후',
    },

    {
        'text': '외계 행성에 복수를 하러 가자!'
    }
]

PAUSE_CONTEXT = [
    {
        'text': ' Press [ESC] to return Game!!'
    },
    {
        'text': '   Your Score is'
    }
]

ENDING_CONTEXT = [
    {
        'text': ' Press [SPACE] to show score!!'
    }
]
