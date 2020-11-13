def print_icecream():
    print("""
                    .oo.
                 oGGGGGGGo
                GGGGGGGGGGG
        .mMMMMMMMMGGGGGEEEEE=
      MMMMMMMMMMMMMMGGEEEEEEE
    MMMMMMMMMMMMMMSOPHIEEEEEEEE
    MMMMMMMMMMMMMMMMMEEEEEEEEEE
    !MMMMMMMMMMMMMOOEEEEEEEEEE
    MMM!MMMMMMMOOOOOOOOOE!=
      MM!!!!!!!!!!!!!!!!!!!
       MM!!!!!!!!!!!!!!!!'
        !M!!!!!!!!!!!!!!!
         MM!!!!!!!!!!!!'
          MM!!!!!!!!!!!
          '!!!!!!!!!!!
           !!!!!!!!!!
           '!!!!!!!!'
            !!!!!!!
             '!!!!'
              !!!!
              '!!'
               !!
               ''
               !
    """)

def print_finance_overview(balance, cost_operating, expenses_icecream, expenses_cones, income, new_balance, play_round):
    print(f"""
    ==========================================================
    ============ Finances Round {play_round:3} ==========================
    Starting money        € {balance:10}
    Operating cost      - € {cost_operating:10}
    Ice expenses        - € {expenses_icecream:10}
    Cone expenses       - € {expenses_cones:10}
    Income              + € {income: 10}
    ----------------------------------------------------------
    Total                 € {new_balance:10}
    """)


