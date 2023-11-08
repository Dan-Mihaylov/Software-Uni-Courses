package com.example.myapplication


import android.content.Context
import android.hardware.Sensor
import android.hardware.SensorEvent
import android.hardware.SensorEventListener
import android.hardware.SensorManager
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.myapplication.databinding.ActivityMainBinding

// In the MainActivity class we inherit the SensorEventListener and we override its functions in order
// to implement it into our app

class MainActivity : AppCompatActivity(), SensorEventListener {
    // Declare and initialize this binding here so you can use it
    // the late init tells andriod that you havet initialized the var but later you gonna do it

    // Just the structure of the screen
    private lateinit  var binding: ActivityMainBinding

    // create sensor manager and a sensor var to use later on
    private var sensorManager: SensorManager? = null
    private var sensor: Sensor? = null


    // to find out what is in the elements we have to inflate it.
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // takes all the values from this class and puts them in the activityMainbinding
        binding = ActivityMainBinding.inflate(layoutInflater)

//        setContentView(R.layout.activity_main)
        // this method says, when you render on the screen you going to show this.. to users.
        setContentView(binding.root)    // Have to change this to the layout root. which has been binded


        // when you write binding you can access all the items from the screen by id
        val username = "Daniel"
        val lasName = "Papazov"

        // Initializing a new User
        val newUser = User(username, lasName)

        binding.btn1.text = "New Text"
        binding.user = newUser

        // getSystemService can get you camera, charger any system service you use
        sensorManager = getSystemService(Context.SENSOR_SERVICE) as SensorManager // cast to SensorManager because you know it is
        sensor = sensorManager?.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)

    }

    // Enter custom logic to tell the app what to do when you turn it in the background.
    // this is the sensormanager you use now, sensor and the action last.

    override fun onResume() {
        super.onResume()
        sensorManager?.registerListener(this, sensor, SensorManager.SENSOR_DELAY_NORMAL)
    }
    // Unregister the listener because if you manipulate UI elements while the event takes place
    // but you have closed the app, when you resume you will crash.

    override fun onPause() {
        super.onPause()
        sensorManager?.unregisterListener(this)
    }

    override fun onSensorChanged(p0: SensorEvent?) {
        val xReading = p0?.values?.get(0) // tilt value on X axis Use .get because maybe there is no values and will throw exception
        val yReading = p0?.values?.get(1) // tilt the values on Y axis
        val zReading = p0?.values?.get(2) // tilt the values on Z axis

        binding.tvUsername.text = "X: $xReading\nY: $yReading\nZ: $zReading"

    }

    override fun onAccuracyChanged(sensor: Sensor?, accuracy: Int) {
    }
}

data class User(
    var firstName: String,
    var lastName: String
)
