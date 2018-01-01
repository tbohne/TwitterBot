from secrets import *
import tweepy
import speedtest

def format_speed(speed):
    units = ['bps', 'Kbps', 'Mbps', 'Gbps']
    unit = 0
    while speed >= 1024:
        speed /= 1024
        unit += 1
    return '%0.2f %s' % (speed, units[unit])

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    servers = []
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download()
    s.upload()

    results_dict = s.results.dict()
    res = ""
    res += "down: " + str(format_speed(results_dict['download'])) + "\n"
    res += "up: " + str(format_speed(results_dict['upload'])) + "\n"
    res += "ping: " + str(format(results_dict['ping'], '.2f')) + " ms"
    print(res)
    api.update_status(res)
