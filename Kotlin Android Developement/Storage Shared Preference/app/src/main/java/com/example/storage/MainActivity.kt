package com.example.storage

import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.storage.databinding.ActivityMainBinding
import com.google.android.material.snackbar.Snackbar

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    // When using getPreferences Func you cannot access them from another view, that is why you need
    // to create a sharedPrefs val and use the getSharedPreferences function passing the
    // val in it.. so you can access those prefs from another view as well.


    val KEY_SAVE_DATA = "KEY_SAVE_DATA"
    val KEY_PREFS_NAME = "KEY_PREFS_NAME"   // Now change preferences to shared prefs and pass that

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.btnSaveData.setOnClickListener {
            val textToSave = binding.etSaveData.text.toString()
            val sharedPrefs = getSharedPreferences(KEY_PREFS_NAME, Context.MODE_PRIVATE)
            val editor = sharedPrefs.edit()
            editor.putString(KEY_SAVE_DATA, textToSave)

            //editor.apply()
            val dataSavedSuccessfully = editor.commit()

            if (dataSavedSuccessfully) {
                Snackbar.make(binding.root, "Data Saved Successfully", Snackbar.LENGTH_LONG).show()
            } else {
                Snackbar.make(binding.root, "Data Failed To Save", Snackbar.LENGTH_LONG).show()
            }
        }

        binding.btnLoadData.setOnClickListener {
            val sharedPrefs = getSharedPreferences(KEY_PREFS_NAME, Context.MODE_PRIVATE)
            val savedText = sharedPrefs.getString(KEY_SAVE_DATA, "No Data To Display")

            binding.etLoadData.setText(savedText)
        }

        // will bind the next page button on click to change to the second activity that we have
        binding.btnNextPage.setOnClickListener {
            val intent = Intent(this, SecondActivity::class.java)
            startActivity(intent)
        }

        // To remove the data that has already been saved in the shared prefs.
        binding.btnClear.setOnClickListener {
            val sharedPrefs = getSharedPreferences(KEY_PREFS_NAME, Context.MODE_PRIVATE)
            val editor = sharedPrefs.edit()
            editor.remove(KEY_SAVE_DATA)
            editor.apply()
            Snackbar.make(binding.root, "Data Cleared", Snackbar.LENGTH_LONG).show()
        }
    }
}