


struct CompressedGene {


  let length: Int
  private let bitVector: CFMutableVitVector

  init(original: String) {

    length = original.count
    //deffault allocator, need 2 * length number o fbits
    bitVector = CFBitVectorCreateMutable(KCFAllocationDefault, length * 2)

  //fills the bit vector with 0s 
    CFBitVectorSetCount(bitVector, length *)

    compress(gene: original)

    }
  }
