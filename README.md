This README describes the custom features build by me (Arne Schwarck) on top of [openpilot](http://github.com/commaai/openpilot) of [comma.ai](http://comma.ai). This fork is optimized for the Toyota RAV4 Hybrid 2016 and for driving in Germany but also works with other cars and in other countries. If you would like to support the developement on this project feel free to https://www.patreon.com/arneschwarck 
- [ ] TODO describe which other cars and countries are known
[![](https://i.imgur.com/UelUjKAh.png)](#)

For a demo of this version of openpilot check the video below:
[![demo of openpilot with this branch](https://img.youtube.com/vi/WKwSq8TPdpo/0.jpg)](https://www.youtube.com/playlist?list=PL3CGUyxys8DuTE1JTkdZwY93ejSfAGxyV)

# Installation
`cd /data; rm -rf openpilot; git clone https://github.com/arne182/openpilot; cd openpilot; git checkout release4; reboot`

<<<<<<< HEAD
still have trouble ?? More info about how to install this fork can be found [here](https://medium.com/@jfrux/comma-eon-installing-a-fork-of-openpilot-5c2b5c134b4b).
=======
---

What is openpilot?
------

[openpilot](http://github.com/commaai/openpilot) is an open source driver assistance system. Currently, openpilot performs the functions of Adaptive Cruise Control (ACC), Automated Lane Centering (ALC), Forward Collision Warning (FCW) and Lane Departure Warning (LDW) for a growing variety of supported [car makes, models and model years](#supported-cars). In addition, while openpilot is engaged, a camera based Driver Monitoring (DM) feature alerts distracted and asleep drivers.

<table>
  <tr>
    <td><a href="https://www.youtube.com/watch?v=mgAbfr42oI8" title="YouTube" rel="noopener"><img src="https://i.imgur.com/kAtT6Ei.png"></a></td>
    <td><a href="https://www.youtube.com/watch?v=394rJKeh76k" title="YouTube" rel="noopener"><img src="https://i.imgur.com/lTt8cS2.png"></a></td>
    <td><a href="https://www.youtube.com/watch?v=1iNOc3cq8cs" title="YouTube" rel="noopener"><img src="https://i.imgur.com/ANnuSpe.png"></a></td>
    <td><a href="https://www.youtube.com/watch?v=Vr6NgrB-zHw" title="YouTube" rel="noopener"><img src="https://i.imgur.com/Qypanuq.png"></a></td>
  </tr>
  <tr>
    <td><a href="https://www.youtube.com/watch?v=Ug41KIKF0oo" title="YouTube" rel="noopener"><img src="https://i.imgur.com/3caZ7xM.png"></a></td>
    <td><a href="https://www.youtube.com/watch?v=NVR_CdG1FRg" title="YouTube" rel="noopener"><img src="https://i.imgur.com/bAZOwql.png"></a></td>
    <td><a href="https://www.youtube.com/watch?v=tkEvIdzdfUE" title="YouTube" rel="noopener"><img src="https://i.imgur.com/EFINEzG.png"></a></td>
    <td><a href="https://www.youtube.com/watch?v=_P-N1ewNne4" title="YouTube" rel="noopener"><img src="https://i.imgur.com/gAyAq22.png"></a></td>
  </tr>
</table>

Integration with Stock Features
------

In all supported cars:
* Stock Lane Keep Assist (LKA) and stock ALC are replaced by openpilot ALC, which only functions when openpilot is engaged by the user.
* Stock LDW is replaced by openpilot LDW.

Additionally, on specific supported cars (see ACC column in [supported cars](#supported-cars)):
* Stock ACC is replaced by openpilot ACC.
* openpilot FCW operates in addition to stock FCW.

openpilot should preserve all other vehicle's stock features, including, but are not limited to: FCW, Automatic Emergency Braking (AEB), auto high-beam, blind spot warning, and side collision warning.

Supported Hardware
------

At the moment, openpilot supports the [EON DevKit](https://comma.ai/shop/products/eon-dashcam-devkit) and the [comma two](https://comma.ai/shop/products/comma-two-devkit). A [car harness](https://comma.ai/shop/products/car-harness) is recommended to connect the EON or comma two to the car. In the future, we'd like to support other platforms as well, like gaming PCs.

Supported Cars
------

| Make      | Model (US Market Reference)   | Supported Package | ACC              | No ACC accel below | No ALC below      |
| ----------| ------------------------------| ------------------| -----------------| -------------------| ------------------|
| Acura     | ILX 2016-18                   | AcuraWatch Plus   | openpilot        | 25mph<sup>6</sup>  | 25mph             |
| Acura     | RDX 2016-18                   | AcuraWatch Plus   | openpilot        | 25mph<sup>6</sup>  | 12mph             |
| Chrysler  | Pacifica 2017-18              | Adaptive Cruise   | Stock            | 0mph               | 9mph              |
| Chrysler  | Pacifica Hybrid 2017-18       | Adaptive Cruise   | Stock            | 0mph               | 9mph              |
| Chrysler  | Pacifica Hybrid 2019-20       | Adaptive Cruise   | Stock            | 0mph               | 39mph             |
| Honda     | Accord 2018-19                | All               | Stock            | 0mph               | 3mph              |
| Honda     | Accord Hybrid 2018-19         | All               | Stock            | 0mph               | 3mph              |
| Honda     | Civic Hatchback 2017-19       | Honda Sensing     | Stock            | 0mph               | 12mph             |
| Honda     | Civic Sedan/Coupe 2016-18     | Honda Sensing     | openpilot        | 0mph               | 12mph             |
| Honda     | Civic Sedan/Coupe 2019        | Honda Sensing     | Stock            | 0mph               | 2mph<sup>4</sup>  |
| Honda     | CR-V 2015-16                  | Touring           | openpilot        | 25mph<sup>6</sup>  | 12mph             |
| Honda     | CR-V 2017-19                  | Honda Sensing     | Stock            | 0mph               | 12mph             |
| Honda     | CR-V Hybrid 2017-2019         | Honda Sensing     | Stock            | 0mph               | 12mph             |
| Honda     | Fit 2018-19                   | Honda Sensing     | openpilot        | 25mph<sup>6</sup>  | 12mph             |
| Honda     | Insight 2019                  | Honda Sensing     | Stock            | 0mph               | 3mph              |
| Honda     | Odyssey 2018-20               | Honda Sensing     | openpilot        | 25mph<sup>6</sup>  | 0mph              |
| Honda     | Passport 2019                 | All               | openpilot        | 25mph<sup>6</sup>  | 12mph             |
| Honda     | Pilot 2016-18                 | Honda Sensing     | openpilot        | 25mph<sup>6</sup>  | 12mph             |
| Honda     | Pilot 2019                    | All               | openpilot        | 25mph<sup>6</sup>  | 12mph             |
| Honda     | Ridgeline 2017-19             | Honda Sensing     | openpilot        | 25mph<sup>6</sup>  | 12mph             |
| Hyundai   | Elantra 2017-19<sup>1</sup>   | SCC + LKAS        | Stock            | 19mph              | 34mph             |
| Hyundai   | Genesis 2018<sup>1</sup>      | All               | Stock            | 19mph              | 34mph             |
| Hyundai   | Santa Fe 2019<sup>1</sup>     | All               | Stock            | 0mph               | 0mph              |
| Jeep      | Grand Cherokee 2016-18        | Adaptive Cruise   | Stock            | 0mph               | 9mph              |
| Jeep      | Grand Cherokee 2019           | Adaptive Cruise   | Stock            | 0mph               | 39mph             |
| Kia       | Optima 2019<sup>1</sup>       | SCC + LKAS        | Stock            | 0mph               | 0mph              |
| Kia       | Sorento 2018<sup>1</sup>      | All               | Stock            | 0mph               | 0mph              |
| Kia       | Stinger 2018<sup>1</sup>      | SCC + LKAS        | Stock            | 0mph               | 0mph              |
| Lexus     | CT Hybrid 2017-18             | All               | Stock<sup>5</sup>| 0mph               | 0mph              |
| Lexus     | ES 2019                       | All               | openpilot        | 0mph               | 0mph              |
| Lexus     | ES Hybrid 2019                | All               | openpilot        | 0mph               | 0mph              |
| Lexus     | IS 2017-2019                  | All               | Stock            | 22mph              | 0mph              |
| Lexus     | IS Hybrid 2017                | All               | Stock            | 0mph               | 0mph              |
| Lexus     | NX Hybrid 2018                | All               | Stock<sup>5</sup>| 0mph               | 0mph              |
| Lexus     | RX 2016-17                    | All               | Stock<sup>5</sup>| 0mph               | 0mph              |
| Lexus     | RX 2020                       | All               | openpilot        | 0mph               | 0mph              |
| Lexus     | RX Hybrid 2016-19             | All               | Stock<sup>5</sup>| 0mph               | 0mph              |
| Subaru    | Crosstrek 2018-19             | EyeSight          | Stock            | 0mph               | 0mph              |
| Subaru    | Impreza 2019-20               | EyeSight          | Stock            | 0mph               | 0mph              |
| Toyota    | Avalon 2016                   | TSS-P             | Stock<sup>5</sup>| 20mph<sup>6</sup>  | 0mph              |
| Toyota    | Avalon 2017-18                | All               | Stock<sup>5</sup>| 20mph<sup>6</sup>  | 0mph              |
| Toyota    | Camry 2018-19                 | All               | Stock            | 0mph<sup>2</sup>   | 0mph              |
| Toyota    | Camry Hybrid 2018-19          | All               | Stock            | 0mph<sup>2</sup>   | 0mph              |
| Toyota    | C-HR 2017-19                  | All               | Stock            | 0mph               | 0mph              |
| Toyota    | C-HR Hybrid 2017-19           | All               | Stock            | 0mph               | 0mph              |
| Toyota    | Corolla 2017-19               | All               | Stock<sup>5</sup>| 20mph<sup>6</sup>  | 0mph              |
| Toyota    | Corolla 2020                  | All               | openpilot        | 0mph               | 0mph              |
| Toyota    | Corolla Hatchback 2019-20     | All               | openpilot        | 0mph               | 0mph              |
| Toyota    | Corolla Hybrid 2020           | All               | openpilot        | 0mph               | 0mph              |
| Toyota    | Highlander 2017-19            | All               | Stock<sup>5</sup>| 0mph               | 0mph              |
| Toyota    | Highlander Hybrid 2017-19     | All               | Stock<sup>5</sup>| 0mph               | 0mph              |
| Toyota    | Highlander 2020               | All               | openpilot        | 0mph               | 0mph              |
| Toyota    | Prius 2016                    | TSS-P             | Stock<sup>5</sup>| 0mph               | 0mph              |
| Toyota    | Prius 2017-19                 | All               | Stock<sup>5</sup>| 0mph               | 0mph              |
| Toyota    | Prius Prime 2017-20           | All               | Stock<sup>5</sup>| 0mph               | 0mph              |
| Toyota    | Rav4 2016                     | TSS-P             | Stock<sup>5</sup>| 20mph<sup>6</sup>  | 0mph              |
| Toyota    | Rav4 2017-18                  | All               | Stock<sup>5</sup>| 20mph<sup>6</sup>  | 0mph              |
| Toyota    | Rav4 2019                     | All               | openpilot        | 0mph               | 0mph              |
| Toyota    | Rav4 Hybrid 2016              | TSS-P             | Stock<sup>5</sup>| 0mph               | 0mph              |
| Toyota    | Rav4 Hybrid 2017-18           | All               | Stock<sup>5</sup>| 0mph               | 0mph              |
| Toyota    | Rav4 Hybrid 2019-20           | All               | openpilot        | 0mph               | 0mph              |
| Toyota    | Sienna 2018                   | All               | Stock<sup>5</sup>| 0mph               | 0mph              |
| Volkswagen| Golf 2016-19<sup>3</sup>      | Driver Assistance | Stock            | 0mph               | 0mph              |

<sup>1</sup>Requires a [panda](https://comma.ai/shop/products/panda-obd-ii-dongle) and open sourced [Hyundai giraffe](https://github.com/commaai/neo/tree/master/giraffe/hyundai), designed for the 2019 Sante Fe; pinout may differ for other Hyundai and Kia models. <br />
<sup>2</sup>28mph for Camry 4CYL L, 4CYL LE and 4CYL SE which don't have Full-Speed Range Dynamic Radar Cruise Control. <br />
<sup>3</sup>Requires a [custom connector](https://community.comma.ai/wiki/index.php/Volkswagen#Integration_at_R242_Camera) for the [car harness](https://comma.ai/shop/products/car-harness) <br />
<sup>4</sup>2019 Honda Civic 1.6L Diesel Sedan does not have ALC below 12mph. <br />

Community Maintained Cars and Features
------

| Make      | Model (US Market Reference)   | Supported Package | ACC              | No ACC accel below | No ALC below |
| ----------| ------------------------------| ------------------| -----------------| -------------------| -------------|
| Buick     | Regal 2018<sup>7</sup>        | Adaptive Cruise   | openpilot        | 0mph               | 7mph         |
| Cadillac  | ATS 2018<sup>7</sup>          | Adaptive Cruise   | openpilot        | 0mph               | 7mph         |
| Chevrolet | Malibu 2017<sup>7</sup>       | Adaptive Cruise   | openpilot        | 0mph               | 7mph         |
| Chevrolet | Volt 2017-18<sup>7</sup>      | Adaptive Cruise   | openpilot        | 0mph               | 7mph         |
| GMC       | Acadia Denali 2018<sup>7</sup>| Adaptive Cruise   | openpilot        | 0mph               | 7mph         |
| Holden    | Astra 2017<sup>7</sup>        | Adaptive Cruise   | openpilot        | 0mph               | 7mph         |

<sup>5</sup>When disconnecting the Driver Support Unit (DSU), openpilot ACC will replace stock ACC. For DSU locations, see [Toyota Wiki page](https://community.comma.ai/wiki/index.php/Toyota). ***NOTE: disconnecting the DSU disables Automatic Emergency Braking (AEB).*** <br />
<sup>6</sup>[Comma Pedal](https://community.comma.ai/wiki/index.php/Comma_Pedal) is used to provide stop-and-go capability to some of the openpilot-supported cars that don't currently support stop-and-go. Here is how to [build a Comma Pedal](https://medium.com/@jfrux/comma-pedal-building-with-macrofab-6328bea791e8). ***NOTE: The Comma Pedal is not officially supported by [comma](https://comma.ai).*** <br />
<sup>7</sup>Requires a [panda](https://comma.ai/shop/products/panda-obd-ii-dongle) and [community built giraffe](https://zoneos.com/volt/). ***NOTE: disconnecting the ASCM disables Automatic Emergency Braking (AEB).*** <br />

Community Maintained Cars and Features are not verified by comma to meet our [safety model](SAFETY.md). Be extra cautious using them. They are only available after enabling the toggle in `Settings->Developer->Enable Community Features`.

Installation Instructions
------

Install openpilot on a EON by entering ``https://openpilot.comma.ai`` during the installer setup.

Follow this [video instructions](https://youtu.be/3nlkomHathI) to properly mount the EON on the windshield. Note: openpilot features an automatic pose calibration routine and openpilot performance should not be affected by small pitch and yaw misalignments caused by imprecise EON mounting.

Before placing the device on your windshield, check the state and local laws and ordinances where you drive. Some state laws prohibit or restrict the placement of objects on the windshield of a motor vehicle.

You will be able to engage openpilot after reviewing the onboarding screens and finishing the calibration procedure.

Limitations of openpilot ALC and LDW
------

openpilot ALC and openpilot LDW do not automatically drive the vehicle or reduce the amount of attention that must be paid to operate your vehicle. The driver must always keep control of the steering wheel and be ready to correct the openpilot ALC action at all times.

While changing lanes, openpilot is not capable of looking next to you or checking your blind spot. Only nudge the wheel to initiate a lane change after you have confirmed it's safe to do so.

Many factors can impact the performance of openpilot ALC and openpilot LDW, causing them to be unable to function as intended. These include, but are not limited to:

* Poor visibility (heavy rain, snow, fog, etc.) or weather conditions that may interfere with sensor operation.
* The road facing camera is obstructed, covered or damaged by mud, ice, snow, etc.
* Obstruction caused by applying excessive paint or adhesive products (such as wraps, stickers, rubber coating, etc.) onto the vehicle.
* The EON is mounted incorrectly.
* When in sharp curves, like on-off ramps, intersections etc...; openpilot is designed to be limited in the amount of steering torque it can produce.
* In the presence of restricted lanes or construction zones.
* When driving on highly banked roads or in presence of strong cross-wind.
* Extremely hot or cold temperatures.
* Bright light (due to oncoming headlights, direct sunlight, etc.).
* Driving on hills, narrow, or winding roads.

The list above does not represent an exhaustive list of situations that may interfere with proper operation of openpilot components. It is the driver's responsibility to be in control of the vehicle at all times.

Limitations of openpilot ACC and FCW
------

openpilot ACC and openpilot FCW are not systems that allow careless or inattentive driving. It is still necessary for the driver to pay close attention to the vehicle’s surroundings and to be ready to re-take control of the gas and the brake at all times.

Many factors can impact the performance of openpilot ACC and openpilot FCW, causing them to be unable to function as intended. These include, but are not limited to:

* Poor visibility (heavy rain, snow, fog, etc.) or weather conditions that may interfere with sensor operation.
* The road facing camera or radar are obstructed, covered, or damaged by mud, ice, snow, etc.
* Obstruction caused by applying excessive paint or adhesive products (such as wraps, stickers, rubber coating, etc.) onto the vehicle.
* The EON is mounted incorrectly.
* Approaching a toll booth, a bridge or a large metal plate.
* When driving on roads with pedestrians, cyclists, etc...
* In presence of traffic signs or stop lights, which are not detected by openpilot at this time.
* When the posted speed limit is below the user selected set speed. openpilot does not detect speed limits at this time.
* In presence of vehicles in the same lane that are not moving.
* When abrupt braking maneuvers are required. openpilot is designed to be limited in the amount of deceleration and acceleration that it can produce.
* When surrounding vehicles perform close cut-ins from neighbor lanes.
* Driving on hills, narrow, or winding roads.
* Extremely hot or cold temperatures.
* Bright light (due to oncoming headlights, direct sunlight, etc.).
* Interference from other equipment that generates radar waves.

The list above does not represent an exhaustive list of situations that may interfere with proper operation of openpilot components. It is the driver's responsibility to be in control of the vehicle at all times.

Limitations of openpilot DM
------

openpilot DM should not be considered an exact measurements of the status of alertness of the driver.

Many factors can impact the performance of openpilot DM, causing it to be unable to function as intended. These include, but are not limited to:
>>>>>>> a5c3340c8dae1d4e3bf0d438661d2dc048b7767e

## Panda flashing

This is done automatically otherwise run (pkill -f boardd; cd /data/openpilot/panda/board; make; reboot) to change the following:
- allowing no disengage on brake and gas for Toyota
- changing acceleration limits for Toyota and
- adapting lane departure warning where it gives you a slight push back into the middle of the lane without needing to be engaged (not yet complete)
- The Panda version is also changed and checked.

## Branches

`release4`: this is the default branch that is most up to date with the openpilot 0.7 release branch. Normally you should use this branch because it has been tested and verified that it is fully working without any issues.

`073-clean`: this is my default testing branch. When I finishing testing/adding new structure, I'll merge this into the
`release4` branch.

`release3`: this is my old branch, that is compatible with openpilot 0.6.

`release2`: this is my old branch, that is compatible with openpilot 0.5.

# Configuration

- You can turn on or off some of the feature by editing `op_edit.py`. run the following command `python /data/openpilot/op_edit.py`

- You can also use live tuner to edit some of the feature live. `op_tune.py` Run the following command `python /data/openpilot/op_tune.py`

# Todo

- [ ] Auto Lane change from Boggyver on release2 and release3 branch. (only used in released 3 and below)

- [ ] Traffic light detection from Littlemountainman

- [ ] Phantom: control open pilot via app like summon ( only on release 3 and below.)

# Features

- Braking:
    - by angle(carstate),
    - by predicted angle in 2.5s(laneplanner),
    - by model(commaai),
    - acceleration measured by steering angle,
    - by curvature (mapd),
    - by mapped sign(stop, yield, roundabouts, bump, hump, traffic light, speed sign, road attribute)
- No disengage for gas, only longitudinal disengage for brake, tire slip or cancel
- Only disengage on main off and on brake at low speed
- Reacting Toyota tssp higher acceleration and braking limits.
- Speed sign reading
- Stock Toyota ldw steering assist
- Cruise set speed available down to 7 kph
- Smooth longitudinal controller also at low speeds
- No disengage for seat belt remove and door opened. Practical for when stopping and then someone opens a door so that the car does not drive into the lead
- No fingerprint compatibility problems. A completely different way to combine and split Fingerprints so that they always work I.e. comma is not supporting rav4h 2019 because of this Fingerprint method. Mine is better
- Custom events and capnp structure so that comma is happy with the drives from my fork
- Forward collision warning actually brakes for you.
- Blind Spot Monitoring for all of the toyota which will be added to control ALCA. For right now it is always on. It will flash rapidly when stopped and if the object is detected.
- Ability to ruduce or Increase curvature Factor from `op_edit.py` (`python /data/openpilot/op_edit.py`) It will also works with eco and sport mode. If using eco mode then it will start breaking early (350 m before) if using sport mode it will slow down little late (150 m).
- Ability to change the SpeedLimit Offset directly from APK. It is based in percentages. For Example, if -1% at 60mph, it will be  approx. 59.4mph, -10% is roughly 54mph etc. (Thank you eFini for the help)
- Dashcam recording button added to the ui. ( it will save video's to the `/data/media/0/video`)
- GPS Accurecy on the Dev UI.
- Live speedlimit_offset in op_tune.py
- If the model detect's cut in it will draw two different chevron to show the user that it see's both of the car.
- Control 3 gas profiles with sport eco and normal buttons on car ( only for toyota).
- [Dynamic distance profiles](https://github.com/ShaneSmiskol/openpilot/tree/stock_additions-devel#dynamic-follow-3-profiles) from Shane (In other word three different dynamic profiles: `traffic`, `relaxed`, `roadtrip`). Profile can be adjusted from either `python /data/openpilot/op_edit.py` or use live tuner to change the profile live (can take up to 4 sec to for new profile to be adjusted) `python /data/openpilot/op_tune.py`.
- Dynamic Follow Button: Now you can change the Dynamic Follow Distance just by tapping the blue button on the bottom right.
- [Dynamic Gas:](https://github.com/ShaneSmiskol/openpilot/tree/stock_additions-devel#dynamic-gas)
        
        - Currently supported vehicles (w/ comma pedal only):
        
        2017 Toyota Corolla (non-TSS2)
        Toyota RAV4 (non-TSS2)
        2019 Honda Pilot
        2016 Honda Civic
        TODO: Need to factor in distance, as it will not accelerate to get closer to the stopped lead if you engage at ~0mph far back from the lead. Also need to add support for vehicles not yet tuned for dynamic gas.

        This aims to provide a smoother driving experience in stop and go traffic (under 20 mph) by modifying the maximum gas that can be applied based on your current velocity and the relative velocity of the lead car. It'll also of course increase the maximum gas when the lead is accelerating to help you get up to speed quicker than stock. And smoother; this eliminates the jerking you get from stock openpilot with comma pedal. It tries to coast if the lead is only moving slowly, it doesn't use maximum gas as soon as the lead inches forward :). When you are above 20 mph, relative velocity and the following distance is taken into consideration.
- ALC w/ BSM : (Automatic Lane Change with Blind spot monitoring) you can now change lane automataclly. It will wait 1 sec before applying ALC. If the BSM detacts objects it will stop the lane change and will take you back in your original lane. Also, it will notify the user on the eon. 


# Licensing

openpilot is released under the MIT license. Some parts of the software are released under other licenses as specified.

Any user of this software shall indemnify and hold harmless Comma.ai, Inc. and its directors, officers, employees, agents, stockholders, affiliates, subcontractors and customers from and against all allegations, claims, actions, suits, demands, damages, liabilities, obligations, losses, settlements, judgments, costs and expenses (including without limitation attorneys’ fees and costs) which arise out of, relate to or result from any use of this software by user.

**THIS IS ALPHA QUALITY SOFTWARE FOR RESEARCH PURPOSES ONLY. THIS IS NOT A PRODUCT.
YOU ARE RESPONSIBLE FOR COMPLYING WITH LOCAL LAWS AND REGULATIONS.
NO WARRANTY EXPRESSED OR IMPLIED.**

---

<img src="https://d1qb2nb5cznatu.cloudfront.net/startups/i/1061157-bc7e9bf3b246ece7322e6ffe653f6af8-medium_jpg.jpg?buster=1458363130" width="75"></img> <img src="https://cdn-images-1.medium.com/max/1600/1*C87EjxGeMPrkTuVRVWVg4w.png" width="225"></img>
