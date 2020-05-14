from time import sleep


def retry(times=3, sleep_secs=10):
    def retry_deco(func):
        def retry_deco_wrapper(*args, **kwargs):
            count = 0
            success = False
            data = None
            while not success and count < times:
                count += 1
                try:
                    data = func(*args, **kwargs)
                    success = True
                except Exception as e:
                    print("get token error:{}, sleep 10s,times={}".format(e, count))
                    sleep(sleep_secs)
                    if count == times:
                        assert False, "get token info failed"
            return data

        return retry_deco_wrapper

    return retry_deco
