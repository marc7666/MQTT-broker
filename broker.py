import logging
import asyncio
from hbmqtt.broker import Broker
import requests


config = {
    'listeners': {
        'default': {
            'type': 'tcp',
            'bind': '127.0.0.1:1883'
        }
    },
    'sys_interval': 10,
    'topic-check': {
        'enabled': False
    }
}

logger = logging.getLogger(__name__)

broker = Broker(config)


@asyncio.coroutine
def startBroker():
    yield from broker.start()

@asyncio.coroutine
def postCloud():
    C = MQTTClient()
    yield from C.connect('mqtt://localhost:9999/')
    yield from C.subscribe([
        ("LINTANGtopic/test", QOS_1)
    ])
    logger.info('Subscribed!')
    try:
        for i in range(1,100):
            message = yield from C.deliver_message()
            packet = message.publish_packet
            print(packet.payload.data.decode('utf-8'))

            mydb = mymongo['mqttpy']
            mycol = mydb['mqttpy']
            mydata = {"message": packet.payload.data.decode('utf-8')}
            x = mycol.insert_one(mydata)
            print('Data saved!')

    except ClientException as ce:
        logger.error("Client exception : %s" % ce)



if __name__ == "__main__":
    formatter = "[%(asctime)s] :: %(levelname)s - %(message)s"
    level = logging.DEBUG
    logging.basicConfig(level=level, format=formatter)
    asyncio.get_event_loop().run_until_complete(startBroker())
    #asyncio.get_event_loop().run_until_complete(postCloud())
    asyncio.get_event_loop().run_forever()
