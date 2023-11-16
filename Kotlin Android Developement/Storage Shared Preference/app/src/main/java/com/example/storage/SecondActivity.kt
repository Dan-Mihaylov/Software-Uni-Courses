package com.example.storage

import android.content.Context
import android.content.SharedPreferences
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.storage.databinding.ActivityMainBinding
import com.example.storage.databinding.ActivitySecondBinding
import com.google.android.material.internal.CheckableImageButton

class SecondActivity: AppCompatActivity() {

    private lateinit var binding: ActivitySecondBinding

    private val KEY_SAVE_DATA = "KEY_SAVE_DATA"
    val KEY_PREFS_NAME = "KEY_PREFS_NAME"   // Now change preferences to shared prefs and pass that

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivitySecondBinding.inflate(layoutInflater) // why we do this?
        setContentView(binding.root)

        binding.btnLoadText.setOnClickListener {
            val sharedPrefs = getSharedPreferences(KEY_PREFS_NAME, Context.MODE_PRIVATE)
            val savedText = sharedPrefs.getString(KEY_SAVE_DATA, "No saved data yet.")
            binding.tvLoadedText.text = savedText
        }

    }
}

// Go to the layout files to create a new layout , activity_second to access the bindings.

// When you make a new activity you have to declare it in the Manifest file...