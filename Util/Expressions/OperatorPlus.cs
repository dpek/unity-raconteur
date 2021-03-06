namespace DPek.Raconteur.Util.Expressions
{
	/// <summary>
	/// Represents an operator that adds the left and right hand arguments.
	/// </summary>
	public class OperatorPlus : Operator
	{
		/// <summary>
		/// Creates a new operator that is represented by the specified symbol.
		/// </summary>
		/// <param name="symbol">
		/// The symbol that represents this operator
		/// </param>
		public OperatorPlus(string symbol) : base(symbol) { }

		/// <summary>
		/// Returns the addition of the left and right hand arguments.
		/// </summary>
		/// <param name="state">
		/// The state to evaluate this operator against.
		/// </param>
		/// <param name="left">
		/// The left hand argument.
		/// </param>
		/// <param name="right">
		/// The right hand argument.
		/// </param>
		public override Value Eval(StoryState state, Value left, Value right)
		{
			return Value.Add(state, left, right);
		}
	}
}
