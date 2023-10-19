import kotlin.math.pow


// 01. Find perimeter and surface of trapeze
//  (a = 15, b = 8.25, c = 4.5, d = 5.5, h = 3.825)

// a. Find Perimeter

val a = 15
val b = 8.25
val c = 4.5
val d = 5.5
val h = 3.825

var perimeter = a + b + c + d
perimeter

// b. Find Surface
var surface = (a + b) / 2 * h
surface



// 02. Find circumference and Surface of a circle
// (r = 12.755, p = 3.14)

val r = 12.755
val p = 3.14

// a. Circumference

var circumference = 2 * p * r
circumference

// b. surface

var circleSurface = p * r.pow(2)
circleSurface

