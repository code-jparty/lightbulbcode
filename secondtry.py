from flask import Flask
from flask import jsonify
from yeelight import Bulb, discover_bulbs
app = Flask(__name__)

ip = None
bulbs = discover_bulbs()
ip = bulbs[0]['ip']


@app.route (/"musictest")
def musictest(tempo):

   transitions = [
           HSVTransition(0, 100, duration=tempo, brightness=100),
           HSVTransition(0, 100, duration=tempo, brightness=1),
           HSVTransition(90, 100, duration=tempo, brightness=100),
           HSVTransition(90, 100, duration=tempo, brightness=1),
           HSVTransition(180, 100, duration=tempo, brightness=100),
           HSVTransition(180, 100, duration=tempo, brightness=1),
           HSVTransition(270, 100, duration=tempo, brightness=100),
           HSVTransition(270, 100, duration=tempo, brightness=1),
   ]

   flow = Flow(
       count=0,  # Cycle forever.
       transitions=transitions
   )

   bulb = Bulb(ip)
   bulb.start_flow(flow)




@app.route("/on")
def on():

   if ip is None:
      return jsonify({'status': 'error', 'message': 'no bulb found'})

   bulb = Bulb(ip)

   try:
      bulb.turn_on()
   except:
      return jsonify({'status': 'error', 'message': 'could not turn on bulb'})

   return jsonify({'status': 'OK'})

@app.route("/off")
def off():

  if ip is None:
      return jsonify({'status': 'error', 'message': 'no bulb found'})

  bulb = Bulb(ip)

  try:
      bulb.turn_off()
  except:
      return jsonify({'status': 'error', 'message': 'could not turn off bulb'})

  return jsonify({'status': 'OK'})

@app.route("/brightness")
def brightness():

   if ip is None:
       return jsonify({'status': 'error', 'message': 'no bulb found'})

   bulb = Bulb(ip)

   try:
       bulb.set_brightness(10)

   except:
       return jsonify({'status': 'error', 'message': 'could not adjust brightness'})


   return jsonify({'status': 'OK'})


@app.route("/party")
def party():

   if ip is None:
       return jsonify({'status': 'error', 'message': 'no bulb found'})

   bulb = Bulb(ip)

   try:

       bulb.set_rgb(255, 0, 0)


   except:
       return jsonify({'status': 'error', 'message': 'could not adjust brightness'})

   return jsonify({'status': 'OK'})





