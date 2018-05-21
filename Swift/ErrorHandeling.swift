
//Error handling is just another way to write an else-if statement to deal with
//error messages


//Design Error(1/3)

enum HeightError: Error {

  case maxHeight 
  case minHeight
 }

 //call function (2/3)

 func checkHeightError(height: Int) throws{

  if height > 200 {
    throw HeightError.maxHeight
  }else if height < 140 {
  throw HeightError.minHeight
  }else {
  print("Enjoy!")
  }


//handle with error (3/3)

do {
  try checkHeightError(height: 400)
 
}catch Heighterror.maxHeight {
  print("You are too tall")

}catch HeightError.minHeight {

  print("You are too short")
}





//print(checkHeightError(height: 150))
