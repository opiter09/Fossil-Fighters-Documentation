# Fossil-Fighters-Documentation
The documentation stuff in Chunk Manager was getting kind of unwieldy, and I discovered the stuff for teams
which is very important but also very much not chunked. So I decided to make a new repo with all my
documentation in it, and take the opportunity to clean some stuff up too.

If you somehow got here without going through Chunk Manager, please do check it out! It can be found at
https://github.com/opiter09/FF1-FFC-Chunk-Manager. Additionally, I have made the following Graphial User
Interface (GUI) file editing tools:
- Spawns: https://github.com/opiter09/Fossil-Fighters-Spawn-Editor
- Teams: https://github.com/opiter09/Fossil-Fighters-Teams-Editor


A note on general terminology (since I have nowhere else to put it):
- The prefix "0x" means that it is a value in hexadecimal notation, i.e in base 16 instead of base 10.
  For example, 0x100 is not 100, but rather (1 * 256) + (0 * 16) + (0 * 1) = 256.
- When I say that everything everywhere is little-endian, I mean that you have to reverse the bytes before
  converting to get the correct value. For example, 2C 01 --> 0x12C --> 300.
- In order to interpret all my locations, you need to be able to read a hex editor's layout. The leftmost
  column represents all digits except the last one, while the topmost row is for the last digit. So to find
  location 0x28, head to row 00000020 and column 08.
- A "chunk" refers to a subset of a file's data which go together, e.g. by all being the data for a single
  vivosaur. For most files, each chunk's start and end can be found at the beginning of the file, in the
  list of locations which are called "pointers." Sometimes, however, chunks each have a fixed length,
  and so such locations are not given.

Finally, here's a spot to credit those other than me who have figured stuff out:
- APOPHENIA
- aquaanimo
- EchoSpaceZ
- Megalo-vania
- Skittle Skitty

I used to list individual contributions, but that was getting rather unwieldy, so just know that everything
is ultimately a community effort.

