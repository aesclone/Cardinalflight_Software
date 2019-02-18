# Mission Planner Test Code

class CurrentState:
    def CurrentState(cs):
        cs.lat = 0
        cs.Mission = 0
        cs.alt = 0
        cs.roll = 0





    print "Start Script"

    for chan in range(1,9):
        Script.SendRC(chan,1500, False)
        Script.SendRC(3, Script.GetParam('RC3_MIN'),True)

    Script.Sleep(5000)

    while cs.lat == 0:
        print 'Waiting for GPS'
        Script.Sleep(1000)


    print 'Got GPS'
    jo = 10 * 13
    print jo
    Script.SendRC(3,1000,False)
    Script.SendRC(4,2000,True)
    cs.Mission.Clear()
    Script.WaitFor('ARMING MOTORS',30000)
    Script.SendRC(4,1500,True)
    print 'Motors Armed!'
    Script.SendRC(3,1700,True)

    while cs.alt < 50:
        Script.Sleep(50)

    Script.SendRC(5,2000,True) # acro
    Script.SendRC(1,2000,False) # roll
    Script.SendRC(3,1370,True) # throttle

    while cs.roll > -45:
        Script.Sleep(5)

    while cs.roll < -45:
        Script.Sleep(5)

    Script.SendRC(5,1500,False) # Stabalize
    Script.SendRC(1,1500,True) # Level roll
    Script.Sleep(2000) # 2 Sec to Stabalize
    Script.SendRC(3,1300,True) # throttle back to land
    thro = 1350

    while cs.alt > .1:
        Script.Sleep(300)

    Script.SendRC(3,1000,False)
    Script.SendRC(4,1000,True)
    Script.WaitFor('DISARMING MOTORS', 30000)
    Script.SendRC(4,1500,True)

    print 'Roll Complete'
