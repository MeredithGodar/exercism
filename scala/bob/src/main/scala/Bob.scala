class Bob {
  def hey(input: String): String = {
    val trimmed_input = input.trim

    trimmed_input match {
      case "" => "Fine. Be that way!"
      case _ => {
        if (trimmed_input.exists(_.isLetter) && trimmed_input.toUpperCase == trimmed_input) "Whoa, chill out!"
        else if (trimmed_input.endsWith("?")) "Sure."
        else "Whatever."
      }
    }
  }
}
