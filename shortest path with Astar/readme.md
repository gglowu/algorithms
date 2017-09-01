# Route finding

Your challenge is to find a route between two points in a city. For each route you are provided with an image of the public transport map that is colour-coded according to the speed of the routes:

| RGB Hex Code    | Speed   | Designation           |
|:---------------:|--------:|-----------------------|
| 0x000000        | 0       | No road               |
| 0xffffff        | 1       | Junction              |
| 0xb03a2e        | 2       | Footpath              |
| 0x6c3483        | 3       | Lane                  |
| 0x2874a6        | 5       | Single Carriage way   |
| 0x117565        | 10      | Dual Carriage way     |
| 0x239b56        | 15      | Motorway              |
| 0xd4ac0d        | 20      | Highspeed rail        |
| 0xd35400        | 1       | Start / finish        |

The start and finish points are labelled in the same way - it does not matter in which direction the route is travelled. The speed of each segment indicates the time taken to travel over one unit length of the route - so the total time between two junctions is equal to the length of the route (in pixels) multiplied by the speed.

For each input map you should produce an image of the same size whose pixels are black everywhere except for the route between start and finish which should be white.

You are provided with 11 maps. map_0000.png to map_0009.png are for small towns. map_0010.png is a special case and represents a very large transport network; can your solution handle this? how would you solve the problem for an arbitrarily large network?