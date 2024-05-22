hints = [
    "The question mentions an object. Find the object in the image. Follow the line starting from this object. The line will connect to another object. Select this object as the answer.",
    "There are several shapes in the image. The question mentions the required count of edges or vertices. Number of shapes in the image containing exactly the specified count of edges or vertices is the required answer.",
    "Find the maximum possible number of identical pieces the pie shown in the image can be divided into.",
    "The scissor cuts the rope along the dotted line as shown in the image. Find the total number of continuous line segments on both sides of the dotted line. The sum of these two numbers is the answer.",
    "Find the number of square tiles that can fill the wall shown in the image.",
    "The image defines a mathematical equation with four numbers. Five numbers are given in question. Find a permutation of these numbers such that the first four satisfy the equation. The last number in this permutation is the answer.",
    "The image shows some exchange equations between objects. Following the equations will give exchange equation for first and last objects. Find the number of last objects obtainable for specified number of first objects in question.",
    "Count the number of triangles in the image.",
    "Person A and B are standing in line. Total number of people in line is T. Position of A is known and relative positions of A and B is known. Find the position of B.",
    "Each cell in the square in the image is given by addition of numbers outside square in corresponding row and column. Find the missing number in black square by reversing these addition equations. Find the number in question mark cell by adding number in corresponding row or column and missing number in black square.",
    "If for p towels, q pins are needed, then for r towels, r * [[q-1] / p] + 1 pins are needed. Find the number of pins needed for specified number of towels.",
    "Positions of animals A and B in the line are given in the question. Find number of animals in the line on the image between animals A and B.",
    "Find the count of each unique number in the image. Find the number of unique numbers with count greater than specified number in question.",
    "A region is described in the question. Find the number of flowers in this region on the image.",
    "Two linear equations for weights can be inferred from the first two boxes shown in the image. Solve these equations to find combined weight of the objects below the third box.",
    "For each option in the question, block the corresponding locations in the image. Return the option in which there is no continuous path from object A to object B mentioned in the question.",
    "Follow the folding patterns instructions shown in the image. Make the cut along the red line. Unfold the paper in the reverse order of instructions. Find the number of pieces of paper.",
    "Remove the polygon in image first that is completely visible. Some new polygons may become completely visible after this. Repeat the process until no polygons are left. Tell the order in which the polygons are removed.",
    "If the animals shown in the image are m columns and n rows apart, then the answer is same as the number of ways to choose n objects from m+n objects.",
    "Identify the required side of the floor in the image. Suppose length of side S of tile is given. Find a stacking of tiles along this side of tile that covers the required side of floor completely. Find the number of tiles in this stack. The answer is this number multiplied by given length.",
    "Find number of hours between departure time and arrival time given in the question. The answer is this number of hours minus the number shown in the image.",
    "Let the greater number in the image be X and smaller number be Y. The answer is [X + Y] / 2.",
    "For each animal shown in the image, find its number of legs. The answer is the sum of the number of legs of all animals shown in the image.",
    "A continuous line is shown next to each option in the image. For each segment, find its length using the grid shown in the image. The answer is the option with the longest continuous line.",
    "Find the time shown on the clock in the image. The answer is this time minus the number of hours given in the question in 12 hour time format.",
    "Count the total number of squares in the image. Identify the number of unique objects mentioned in the question. The answer is the number of squares divided by the number of unique objects.",
    "Number of forward jumps and backward jumps is given in question. Keep making forward jumps first and then backward jumps. Stop when the end of the fence shown in the image is reached. Find the number of jumps made. Answer is the number of jumps multiplied by the time taken for each jump.",
    "3 linear equations are shown in the image. Solve these equations to find value of each object. Substitute these values in equation 4 shown in the image to find the number to replace the question mark.",
    "Count total number of objects in the grid shown in the image. Find the length of the grid shown in the image. Suppose we want N objects in each row and column of the grid shown in the image. Answer is N*[length of grid]-[total number of objects in the grid].",
    "If there are N medium boxes in a large box and M small boxes in each medium box, then answer is N*M+N+1",
    "The count of three different animals is given in the image. Let the number of these animals be X, Y and Z. If we want to change Y such that the total number of animals is N*Y, then the answer is [X+Z]/[N-1]-Y.",
    "Identify the letter in the image that is not present in the word given in the question.",
    "Find the number of black circles in the image. Find the answer by dividing this number by two.",
    "Find the number of matchsticks in the image. Do not confuse the matchsticks with the background image.",
    "Identify the color corresponding to point O using color scheme given in the image. Identify location of point O in the labyrinth in the image. Find the points reachable from point O in the labyrinth. Find the letters corresponding to the reachable points using the colorscheme given in the image. Select the correct option.",
    "Find the maximum number of circle in the image such that they do no touch each other. Do this by selecting maximum number of alternate circles in the image.",
    "Find the path from A to B which passes through minimum number of doors in the image.",
    "The number of rooms in which the light was lit is the number of windows that are lit divided by the number of windows in each room. The number of rooms in which the light was not lit is the number of windows that are not lit divided by the number of windows in each room. The sum of rooms where light was lit and rooms where light was not lit is the total number of rooms.",
    "Follow the path from point A in the image to point B in the image. If person is going down on path, left of person is right in image and right of person is left in image. If person is going right on path, left of person is up in the image and right of person is down in the image. Similarly if the person is going left or up on the path. Find the letters that on the left or right of the person as required in the question.",
    "Find the smallest square that can fit all the square tiles in the image. The side of this square is the maximum vertical of horizontal distance between two tiles. Find the number of tiles that need to be added to image to convert it into this square.",
    "For each animal in the image, find the side that the animal is facing. Count the number of animals in that side. The answer is the sum of these counts.",
    "Identify the circles in the image that are mentioned in the question. These can be all the circles or circles having particular colour. Find the number of dots in these circles using the image.",
    "A specific region in the image is described in the question. Find the numbers in the image in this region. Find the sum of these numbers.",
    "The question mentions whether the shortest or longest strip is required. Identify this strip in the image. Find the letter closest to that strip in the image. This letter is the correct option.",
    "The question mentions the colour of the cubes whose count is required. Count the number of cubes of this colour in the image. This count is the answer.",
    "The image displays a mathematical equation. Numbers are given in the question. Find an arrangement of these numbers such that they satisfy the equation in the image. The middle number in this arrangement is the answer.",
    "The total number of slices is number of eatables multiplied by number of slices in each eatable. The number of humans is the number of guests plus one. The number of slices eaten is the number of humans multiplied by the number of slices eaten by each human. The number of slices not eaten is the total number of slices minus the number of slices eaten.",
    "The question mentions the starting and ending numbers in the image. Find these numbers in the image. The question also mentions the number of jumps allowed. Find number of unique ways to reach from starting location to ending location in exactly the specified number of jumps.",
    "Some numbers are given in the question. Find an arrangement of these numbers by placing one number in each circle in the image such that the sum of numbers in the row and column is same. A circle of specific colour is mentioned in the question. The number in this circle in the arrangement found earlier is the answer.",
    "There are squares of two colours in the image. Count the number of squares of each colour in the image. The answer is the sum or difference of these numbers based on what is asked in the question.",
    "Some animals are shown in the image. Each animal corresponds to the letter closest to it in the image. Select the middle animal when the animals are ordered as per their size in the image. The letter corresponding to this middle animal is the answer.",
    "Total number of squares is mentioned in the question. Count the number of squares shown in the image. The answer is the total number of squares mentioned in the question minus the number of squares shown in the image.",
    "Count the total number of circles shown in the image. Count the number of circles surrounding the animal in the image. Number of circles not surrounding the animal is total number of circles in the image minus number of circles surrounding the animal in the image. The answer is the number of circles surrounding the animal or the number of circles not surrounding the animal as required in the question.",
    "A word is mentioned in the question for which letters have to be picked in the image. Start from the first letter in the word and keep moving to the next letter in the word along the shortest path. The total length of the path traversed is the answer.",
    "Middle stick refers to total number of sticks divided by 2. Remove the stick in the image first that is completely visible. Some new sticks may become completely visible after this. Repeat the process until the middle stick is reached. Tell the color of the middle stick using the color scheme shown in the image.",
    "Three birds are shown in the image. One bird caught no more than X number of bugs. Another bird caught at least Y number of bugs. The answer is three times X-Y minus 5.",
    "Fill the grey boxes in the image by following the checkered pattern in the image. A region is described in the question relative to the thick line in the image. Count the required colour tiles that replace the grey tiles in the region relative to the thick line in the image.",
    "Find the two numbers inside the circle in the image and successively apply the operations outside the circle in circular and anti-circular order till a blank square is reached outside the circle. Two resultant numbers will be found. The difference of these numbers is the answer.",
    "A mathematical expression is shown in the image. Each polygon in the image denotes a position to place a digit. Adjacent polygons form double digit numbers. Some digits are given in the question. Place the larger digits in the tens positions of double digit numbers and place the smaller digits in the ones positions. Find the answer by evaluating the expression thus formed.",
    "A person want to multiply all the numbers from number A to number B using their calculator. The answer is 3 times [B-A].",
    "Count the number of each type of icon in left polygon in the image. Count the number of each type of icon in right polygon in the image. Answer is the maximum quotient of number of any icon in the right polygon divided by the corresponding number in the left polygon.",
    "For each option, place the item in consideration in the position specified by the option in the image. Check if a possible placement exists in the image that follows the instructions in the question. The answer is the option for which no possible placement of objects exists in the image.",
    "Some numbers are given in the question. Find all possible arrangements of these numbers by placing one number in each circle in the image such that the sum of numbers in the row and column is same. A circle of specific colour is mentioned in the question. The option consisting the possible numbers in this circle in the arrangements found earlier is the answer.",
    "Divide the circle in the image into the number of slices specified in the question. The answer is the number of slices that fill the empty region in the circle in the image.",
    "The question mentions an alphabet. Find the alphabet in the image. Follow the line starting from this alphabet in the image. The line will connect to a number. Select this number as the answer.",
    "Find the polygon in the image which has no arrows pointing towards it. The alphabet in this polygon is the answer.",
    "Find the number of steps in the image. One animal goes up X steps each time and another animal goes down Y steps each time. The answer is the number of steps in the image divided by [X+Y] multiplied by X.",
    "Look at the first coloured rectangle in the image. The question specifies a transformation that should be applied to this rectangle like flipping about an edge. Apply this transformation. The other rectangles in the image correspond the options closes to them in the image. Find the rectangle that is same as the transformed rectangle in the image. This is the correct option.",
    "Two cards are shown in the left of the image. the first card has some black dots and second card has some colored dots. Remove all colored dots from the second card where there is no black dot on the first card in the corresponding location. Select the card from the cards on the right in the image that looks same as second card after this removal. The letter closest to the selected card on the image is the answer.",
    "Identify the location of the question mark in the image. Options are displayed as cards on the image. Look at the row and column in which the question mark is present in the grid. Select the option on which colour and number of dots is different from all squares in the row and column corresponding to the question mark.",
    "Cabin with digit A is opposite to cabin with digit A. Cabin opposite to cabin with digit X is 2*A-X.",
    "Find the square with the question mark in the image. Apart from this square, there are squares of two different colours in the image. Find the count of these squares. Let that be A and B. Some numbers are given in the question. Remove one number from these numbers such that the remaining numbers can be split into groups of size A and B such that sum of numbers in each group is same as the sum specified in the question. The number that was removed is the answer.",
    "There are supposed to be N houses on every circle and every straight line in the image. N is given in the question. Find the number of houses on every circle in the image. Find the number of houses on every straight line on the image. Find the circle that does not have N houses. Find the straight line that does not have N houses. There is a letter written at the intersection of this circle and this straight line. This letter is the answer.",
    "Six numbers from A to B are written on the cube shown in the image. A and B are given in the question. We need to find the number on opposite side of number P. Number P is also given in the question. If B is written on the cube in the image, then the answer is A+B-P. If A+3 is written on the cube in the image, then the answer is A+B-P-1. Otherwise the answer can be either A+B-P or A+B-P-1.",
    "A person formed a cube with some bricks of colour 1 and N bricks of colour 2 as given in question. Count the number of bricks of colour 2 that are visible in the cube shown in the image. The answer is N minus number of bricks of colour 2 that are visible in the cube shown in the image.",
    "There are two flowers shown in the image. Each flower has numbers written on it. Find the sum of numbers on each flower shown in the image. The answer is the difference of these two sums.",
    "There is a circle on the top left of the image. Some colourful dots are present on this circle in the image. Find another circle in the image that has dots in the same location as the dots on the circle in the top left of the image. The letter closest to this circle in the image is the answer.",
    "Find the number of spikes on the left star in the image. Find the number of spikes on the right star in the image. The answer is the number of spikes on the right star divided by the number of spikes on the left star.",
    "A part of a circle is shown in the image. This circle is divided into some slices. Find the number of slices that will complete the circle.",
    "Find the number of animals in the left of the image. Find the number of animals in the right of the image. The answer is the difference of these two numbers divided by two.",
    "When seen from top, a rectangle in the image will be visible if there are no rectangles above this rectangle in the image that are bigger than this rectangle. Find the number of rectangles that are visible in the image when seen from top.",
    "Remove that object in image first that is completely visible. Some new objects may become completely visible after this. Repeat the process until only one object is left. The answer is the letter closest to the object that is left in the image.",
    "Copy the pattern shown on the grid in the image. The answer is the letter that lies on the copied pattern in the image.",
    "At the bottom of the image, some puzzle pieces are shown and on the top of the image, the puzzle is shown. Find the puzzle piece that is not present in the puzzle in the image. The letter closest to this puzzle piece is the answer.",
    "From first five circles in the image, five linear equations can be formed. Solve these equations to find the number of points for the last circle in the image. The answer is the number of points for the last circle in the image,",
    "A right hand when seen from the front has thumb on the left and fingers on the right. A right hand when seen from the back has thumb on the right and fingers on the left. Find the number of right hands in the image. Find the total number of hands in the image. The number of left hands is the total number of hands in the image minus the number of right hands in the image. The answer is the number of right hands or the number of left hands as asked in the question.",
    "The number of people seeking shelter is given in the question. Count the number of blue circles in the image. The answer is the number of people seeking shelter minus twice the number of blue circle in the image.",
    "The cost of one chocolate is given in the question. Count the number of chocolates in the image. The discounted price of this many chocolates is also given in the image. Total number of dollars is given in the question. Find the maximum number of chocolates that can be bought at the discounted price. Then buy chocolates with the remaining dollars. The answer is the total number of chocolates thus bought.",
    "Find the count of distinct numbers bigger than number A but smaller than number B with the digits that are specified in the question.",
    "Count the number of coins on the left of the image. Let that A. Count the number of coins on the right of the image. Let that be B. A person adds X number of coins to the left and Y number of coins to the right everyday. Answer is [B-A] divided by [Y-X].",
    "A person has P, Q, R, S numbers of a fruits of colours A, B, C, D. The person splits every fruit that is not of colour B in half and then splits every fruit that is not of colour C in half. The answer is 4 times [P+S] plus 2 times [R+S].",
    "The length and width of each rectangle is given in the question. Either the width or height of the arrangement in the image is asked in the question. Find a stacking of tiles in the image that spans the width or height. Find the width or height of the arrangement by finding the length of the stack using the length and width of individual rectangles given in the question.",
    "In the question, it is given that the distance from the house of person A to the house of person B is X and distance from the house of person A to the house of person C is Y. The image shows the distance from the house of person A to the crossroads. Read that from the image and let that be Z. Answer is X+Y minus 2*Z.",
    "Two numbers are present in the image. The answer is the difference of these two numbers.",
    "Find the letter in the center most location of the image. This letter is the correct option.",
    "Count the total number of kids in the image. All kids except the two kids at the end on both sides are holding another child's hand with both hands. If the kid on the left end is facing back, then he is grasping another kid's hand with his right hand, otherwise he is grasping another kid's hand with his left hand. If the kid on the right end is facing back, then he is grasping another kid's hand with his left hand, otherwise he is grasping another kid's hand with his right hand. Find the number of kids holding another kids' hands with their left or right hand as required by the question.",
    "The scissor cuts the rope along the dotted line as shown in the image. Find the total number of continuous line segments on both sides of the dotted line. The sum of these two numbers is the answer.",
    "The distance travelled by the animal or vehicle is given in the question. A road is shown in the image. The length of each segment of the road is also given in the image. The animal or vehicle is at the starting position in the image. From this position, move along the arrow for the total distance given in the question to reach the final position. The letter located closest to this final position is the correct answer.",
    "Count the number of each type of icon in left polygon in the image. Count the number of each type of icon in right polygon in the image. Answer is the sum of the differences of the numbers of each type of icon in the two polygons in the image.",
    "An encryption is given in the question. Every two letters of this encryption form a single letter in the decryption. The first letter specifies the row number and the second letter specifies the column number. For each pair in the encryption given in the question, lookup the grid in the image with first letter as row number and the second number as column number to decrypt the encryption. The decryption is the answer.",
    "Read the numbers shown in the image. Split these numbers into two groups such that sum of numbers in both groups is equal. The number in the same group as the number mentioned in the question is the answer."
]






















