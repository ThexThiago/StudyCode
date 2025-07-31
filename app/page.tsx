"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { BookOpen, Calendar, CheckCircle, Clock, Code, Plus, Target, Trash2 } from "lucide-react"

interface StudyTopic {
  id: string
  title: string
  description: string
  category: string
  difficulty: "Iniciante" | "Intermediário" | "Avançado"
  estimatedHours: number
  completed: boolean
  resources: string[]
  createdAt: Date
}

interface StudySession {
  id: string
  topicId: string
  date: Date
  duration: number
  notes: string
}

export default function StudyPlatform() {
  const [topics, setTopics] = useState<StudyTopic[]>([
    {
      id: "1",
      title: "React Hooks",
      description: "Aprender useState, useEffect e hooks customizados",
      category: "Frontend",
      difficulty: "Intermediário",
      estimatedHours: 8,
      completed: false,
      resources: ["https://react.dev/reference/react", "Curso Udemy React"],
      createdAt: new Date("2024-01-15"),
    },
    {
      id: "2",
      title: "Node.js APIs",
      description: "Criar APIs RESTful com Express e MongoDB",
      category: "Backend",
      difficulty: "Intermediário",
      estimatedHours: 12,
      completed: true,
      resources: ["Documentação Express", "MongoDB University"],
      createdAt: new Date("2024-01-10"),
    },
  ])

  const [sessions, setSessions] = useState<StudySession[]>([
    {
      id: "1",
      topicId: "1",
      date: new Date("2024-01-20"),
      duration: 2,
      notes: "Estudei useState e useEffect básico",
    },
    {
      id: "2",
      topicId: "2",
      date: new Date("2024-01-18"),
      duration: 3,
      notes: "Implementei autenticação JWT",
    },
  ])

  const [newTopic, setNewTopic] = useState({
    title: "",
    description: "",
    category: "",
    difficulty: "Iniciante" as const,
    estimatedHours: 1,
    resources: "",
  })

  const [newSession, setNewSession] = useState({
    topicId: "",
    duration: 1,
    notes: "",
  })

  const [isTopicDialogOpen, setIsTopicDialogOpen] = useState(false)
  const [isSessionDialogOpen, setIsSessionDialogOpen] = useState(false)

  const addTopic = () => {
    if (!newTopic.title || !newTopic.category) return

    const topic: StudyTopic = {
      id: Date.now().toString(),
      title: newTopic.title,
      description: newTopic.description,
      category: newTopic.category,
      difficulty: newTopic.difficulty,
      estimatedHours: newTopic.estimatedHours,
      completed: false,
      resources: newTopic.resources
        .split(",")
        .map((r) => r.trim())
        .filter((r) => r),
      createdAt: new Date(),
    }

    setTopics([...topics, topic])
    setNewTopic({
      title: "",
      description: "",
      category: "",
      difficulty: "Iniciante",
      estimatedHours: 1,
      resources: "",
    })
    setIsTopicDialogOpen(false)
  }

  const addSession = () => {
    if (!newSession.topicId) return

    const session: StudySession = {
      id: Date.now().toString(),
      topicId: newSession.topicId,
      date: new Date(),
      duration: newSession.duration,
      notes: newSession.notes,
    }

    setSessions([...sessions, session])
    setNewSession({
      topicId: "",
      duration: 1,
      notes: "",
    })
    setIsSessionDialogOpen(false)
  }

  const toggleTopicCompletion = (id: string) => {
    setTopics(topics.map((topic) => (topic.id === id ? { ...topic, completed: !topic.completed } : topic)))
  }

  const deleteTopic = (id: string) => {
    setTopics(topics.filter((topic) => topic.id !== id))
    setSessions(sessions.filter((session) => session.topicId !== id))
  }

  const getTopicSessions = (topicId: string) => {
    return sessions.filter((session) => session.topicId === topicId)
  }

  const getTotalStudyHours = () => {
    return sessions.reduce((total, session) => total + session.duration, 0)
  }

  const getCompletedTopics = () => {
    return topics.filter((topic) => topic.completed).length
  }

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty) {
      case "Iniciante":
        return "bg-green-100 text-green-800"
      case "Intermediário":
        return "bg-yellow-100 text-yellow-800"
      case "Avançado":
        return "bg-red-100 text-red-800"
      default:
        return "bg-zinc-900 text-gray-800"
    }
  }

  const getProgressPercentage = () => {
    if (topics.length === 0) return 0
    return Math.round((getCompletedTopics() / topics.length) * 100)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-900 via-blue-800 to-indigo-900 p-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2 flex items-center justify-center gap-2">
            <Code className="w-8 h-8 text-blue-600" />
            StudyCode
          </h1>
          <p className="text-gray-600">Organize seus estudos de programação de forma eficiente</p>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
          <Card>
            <CardContent className="p-4">
              <div className="flex items-center gap-2">
                <BookOpen className="w-5 h-5 text-blue-600" />
                <div>
                  <p className="text-sm text-gray-600">Total de Tópicos</p>
                  <p className="text-2xl font-bold">{topics.length}</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="p-4">
              <div className="flex items-center gap-2">
                <CheckCircle className="w-5 h-5 text-green-600" />
                <div>
                  <p className="text-sm text-gray-600">Concluídos</p>
                  <p className="text-2xl font-bold">{getCompletedTopics()}</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="p-4">
              <div className="flex items-center gap-2">
                <Clock className="w-5 h-5 text-purple-600" />
                <div>
                  <p className="text-sm text-gray-600">Horas Estudadas</p>
                  <p className="text-2xl font-bold">{getTotalStudyHours()}h</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="p-4">
              <div className="flex items-center gap-2">
                <Target className="w-5 h-5 text-orange-600" />
                <div>
                  <p className="text-sm text-gray-600">Progresso</p>
                  <p className="text-2xl font-bold">{getProgressPercentage()}%</p>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Progress Bar */}
        <Card className="mb-8">
          <CardContent className="p-6">
            <div className="flex items-center justify-between mb-2">
              <h3 className="text-lg font-semibold">Progresso Geral</h3>
              <span className="text-sm text-gray-600">
                {getCompletedTopics()} de {topics.length} tópicos
              </span>
            </div>
            <Progress value={getProgressPercentage()} className="h-3" />
          </CardContent>
        </Card>

        <Tabs defaultValue="topics" className="w-full">
          <TabsList className="grid w-full grid-cols-2">
            <TabsTrigger value="topics">Tópicos de Estudo</TabsTrigger>
            <TabsTrigger value="sessions">Sessões de Estudo</TabsTrigger>
          </TabsList>

          <TabsContent value="topics" className="space-y-4">
            <div className="flex justify-between items-center">
              <h2 className="text-2xl font-bold">Tópicos de Estudo</h2>
              <Dialog open={isTopicDialogOpen} onOpenChange={setIsTopicDialogOpen}>
                <DialogTrigger asChild>
                  <Button>
                    <Plus className="w-4 h-4 mr-2" />
                    Novo Tópico
                  </Button>
                </DialogTrigger>
                <DialogContent>
                  <DialogHeader>
                    <DialogTitle>Adicionar Novo Tópico</DialogTitle>
                    <DialogDescription>Crie um novo tópico de estudo para organizar seu aprendizado</DialogDescription>
                  </DialogHeader>
                  <div className="grid gap-4 py-4">
                    <div className="grid gap-2">
                      <Label htmlFor="title">Título</Label>
                      <Input
                        id="title"
                        value={newTopic.title}
                        onChange={(e) => setNewTopic({ ...newTopic, title: e.target.value })}
                        placeholder="Ex: React Hooks"
                      />
                    </div>
                    <div className="grid gap-2">
                      <Label htmlFor="description">Descrição</Label>
                      <Textarea
                        id="description"
                        value={newTopic.description}
                        onChange={(e) => setNewTopic({ ...newTopic, description: e.target.value })}
                        placeholder="Descreva o que você vai estudar..."
                      />
                    </div>
                    <div className="grid grid-cols-2 gap-4">
                      <div className="grid gap-2">
                        <Label htmlFor="category">Categoria</Label>
                        <Input
                          id="category"
                          value={newTopic.category}
                          onChange={(e) => setNewTopic({ ...newTopic, category: e.target.value })}
                          placeholder="Ex: Frontend"
                        />
                      </div>
                      <div className="grid gap-2">
                        <Label htmlFor="difficulty">Dificuldade</Label>
                        <Select
                          value={newTopic.difficulty}
                          onValueChange={(value: any) => setNewTopic({ ...newTopic, difficulty: value })}
                        >
                          <SelectTrigger>
                            <SelectValue />
                          </SelectTrigger>
                          <SelectContent>
                            <SelectItem value="Iniciante">Iniciante</SelectItem>
                            <SelectItem value="Intermediário">Intermediário</SelectItem>
                            <SelectItem value="Avançado">Avançado</SelectItem>
                          </SelectContent>
                        </Select>
                      </div>
                    </div>
                    <div className="grid gap-2">
                      <Label htmlFor="hours">Horas Estimadas</Label>
                      <Input
                        id="hours"
                        type="number"
                        min="1"
                        value={newTopic.estimatedHours}
                        onChange={(e) => setNewTopic({ ...newTopic, estimatedHours: Number.parseInt(e.target.value) })}
                      />
                    </div>
                    <div className="grid gap-2">
                      <Label htmlFor="resources">Recursos (separados por vírgula)</Label>
                      <Textarea
                        id="resources"
                        value={newTopic.resources}
                        onChange={(e) => setNewTopic({ ...newTopic, resources: e.target.value })}
                        placeholder="Ex: Documentação oficial, Curso Udemy, YouTube"
                      />
                    </div>
                  </div>
                  <DialogFooter>
                    <Button onClick={addTopic}>Adicionar Tópico</Button>
                  </DialogFooter>
                </DialogContent>
              </Dialog>
            </div>

            <div className="grid gap-4">
              {topics.map((topic) => (
                <Card
                  key={topic.id}
                  className={`transition-all ${topic.completed ? "bg-green-50 border-green-200" : ""}`}
                >
                  <CardHeader>
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <div className="flex items-center gap-2 mb-2">
                          <CardTitle className={topic.completed ? "line-through text-gray-500" : ""}>
                            {topic.title}
                          </CardTitle>
                          <Badge className={getDifficultyColor(topic.difficulty)}>{topic.difficulty}</Badge>
                          <Badge variant="outline">{topic.category}</Badge>
                        </div>
                        <CardDescription>{topic.description}</CardDescription>
                      </div>
                      <div className="flex items-center gap-2">
                        <Button
                          variant={topic.completed ? "default" : "outline"}
                          size="sm"
                          onClick={() => toggleTopicCompletion(topic.id)}
                        >
                          <CheckCircle className="w-4 h-4" />
                        </Button>
                        <Button variant="outline" size="sm" onClick={() => deleteTopic(topic.id)}>
                          <Trash2 className="w-4 h-4" />
                        </Button>
                      </div>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <div className="flex items-center justify-between text-sm text-gray-600 mb-3">
                      <span className="flex items-center gap-1">
                        <Clock className="w-4 h-4" />
                        {topic.estimatedHours}h estimadas
                      </span>
                      <span className="flex items-center gap-1">
                        <Calendar className="w-4 h-4" />
                        {getTopicSessions(topic.id).length} sessões
                      </span>
                    </div>
                    {topic.resources.length > 0 && (
                      <div>
                        <p className="text-sm font-medium mb-2">Recursos:</p>
                        <div className="flex flex-wrap gap-1">
                          {topic.resources.map((resource, index) => (
                            <Badge key={index} variant="secondary" className="text-xs">
                              {resource}
                            </Badge>
                          ))}
                        </div>
                      </div>
                    )}
                  </CardContent>
                </Card>
              ))}
            </div>
          </TabsContent>

          <TabsContent value="sessions" className="space-y-4">
            <div className="flex justify-between items-center">
              <h2 className="text-2xl font-bold">Sessões de Estudo</h2>
              <Dialog open={isSessionDialogOpen} onOpenChange={setIsSessionDialogOpen}>
                <DialogTrigger asChild>
                  <Button>
                    <Plus className="w-4 h-4 mr-2" />
                    Nova Sessão
                  </Button>
                </DialogTrigger>
                <DialogContent>
                  <DialogHeader>
                    <DialogTitle>Registrar Sessão de Estudo</DialogTitle>
                    <DialogDescription>
                      Registre uma nova sessão de estudo para acompanhar seu progresso
                    </DialogDescription>
                  </DialogHeader>
                  <div className="grid gap-4 py-4">
                    <div className="grid gap-2">
                      <Label htmlFor="topic">Tópico</Label>
                      <Select
                        value={newSession.topicId}
                        onValueChange={(value) => setNewSession({ ...newSession, topicId: value })}
                      >
                        <SelectTrigger>
                          <SelectValue placeholder="Selecione um tópico" />
                        </SelectTrigger>
                        <SelectContent>
                          {topics.map((topic) => (
                            <SelectItem key={topic.id} value={topic.id}>
                              {topic.title}
                            </SelectItem>
                          ))}
                        </SelectContent>
                      </Select>
                    </div>
                    <div className="grid gap-2">
                      <Label htmlFor="duration">Duração (horas)</Label>
                      <Input
                        id="duration"
                        type="number"
                        min="0.5"
                        step="0.5"
                        value={newSession.duration}
                        onChange={(e) => setNewSession({ ...newSession, duration: Number.parseFloat(e.target.value) })}
                      />
                    </div>
                    <div className="grid gap-2">
                      <Label htmlFor="notes">Anotações</Label>
                      <Textarea
                        id="notes"
                        value={newSession.notes}
                        onChange={(e) => setNewSession({ ...newSession, notes: e.target.value })}
                        placeholder="O que você estudou nesta sessão?"
                      />
                    </div>
                  </div>
                  <DialogFooter>
                    <Button onClick={addSession}>Registrar Sessão</Button>
                  </DialogFooter>
                </DialogContent>
              </Dialog>
            </div>

            <div className="grid gap-4">
              {sessions.map((session) => {
                const topic = topics.find((t) => t.id === session.topicId)
                return (
                  <Card key={session.id}>
                    <CardContent className="p-4">
                      <div className="flex items-start justify-between">
                        <div className="flex-1">
                          <h3 className="font-semibold">{topic?.title}</h3>
                          <p className="text-sm text-gray-600 mb-2">{session.notes}</p>
                          <div className="flex items-center gap-4 text-sm text-gray-500">
                            <span className="flex items-center gap-1">
                              <Calendar className="w-4 h-4" />
                              {session.date.toLocaleDateString("pt-BR")}
                            </span>
                            <span className="flex items-center gap-1">
                              <Clock className="w-4 h-4" />
                              {session.duration}h
                            </span>
                          </div>
                        </div>
                        <Badge className={getDifficultyColor(topic?.difficulty || "Iniciante")}>
                          {topic?.category}
                        </Badge>
                      </div>
                    </CardContent>
                  </Card>
                )
              })}
            </div>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  )
}
