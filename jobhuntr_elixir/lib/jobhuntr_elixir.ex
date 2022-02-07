defmodule JobhuntrElixir do
  use Hound.Helpers

  @moduledoc """
  Documentation for `JobhuntrElixir`.
  """

  def start, do: Hound.start_session()

  def indeed_search do
    navigate_to("http://au.indeed.com/")
    fill_field({:id, "text-input-what"}, "Linux")
    # |> fill_field("Linux")

    # submit_element(element)
  end

  def render do
    filename = "/home/nan0scho1ar/repos/me/jobhuntr/jobhuntr_elixir/webpage.html"
    file = File.open!(filename, [:read, :utf8, :write])
    IO.puts(file, page_source())
    File.close(file)
  end
end
